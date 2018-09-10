import os
import json
from lxml import etree
from PIL import Image

def write_xml(image_path, scene_path, output_dir):
    """
    Args:
        image_path: string
        scene_path: string
        output_dir: string
    Returns:
        output_path: string
    """
    root = etree.Element("annotation")
    etree.SubElement(root, "folder").text = os.path.dirname(image_path)
    etree.SubElement(root, "filename").text = os.path.basename(image_path)

    source = etree.SubElement(root, "source")
    etree.SubElement(source, "database").text = "CLEVR_BB"

    size = etree.SubElement(root, "size")
    img = Image.open(image_path)
    etree.SubElement(size, "width").text = str(img.size[0])
    etree.SubElement(size, "height").text = str(img.size[1])
    etree.SubElement(size, "depth").text = '3'

    etree.SubElement(root, "segmented").text = '0'

    scene_dict = json.load(open(scene_path))
    for obj_dict in scene_dict['objects']:
        obj_tree_node = etree.SubElement(root, 'object')
        obj_class = obj_dict['size'] + '_' + obj_dict['color'] + '_' + obj_dict['material'] + '_' + obj_dict['shape']
        etree.SubElement(obj_tree_node, 'name').text = obj_class
        etree.SubElement(obj_tree_node, "pose").text = "unspecified"
        etree.SubElement(obj_tree_node, "truncated").text = '0'
        etree.SubElement(obj_tree_node, "difficult").text = '0'
        bndbox = etree.SubElement(obj_tree_node, "bndbox")
        etree.SubElement(bndbox, "xmin").text = str(obj_dict['x'])
        etree.SubElement(bndbox, "ymin").text = str(obj_dict['y'])
        etree.SubElement(bndbox, "xmax").text = str(obj_dict['x']+obj_dict['width'])
        etree.SubElement(bndbox, "ymax").text = str(obj_dict['y']+obj_dict['height'])

    tree = etree.ElementTree(root)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = output_dir + '/' + os.path.splitext(os.path.basename(image_path))[0] + '.xml'
    tree.write(output_path, pretty_print=True)
    return output_path

def generate_all_class_label():
    properties_json_path = './data/properties.json'
    with open(properties_json_path, 'r') as f:
        properties = json.load(f)
        sizes = properties['sizes'].keys()
        colors = properties['colors'].keys()
        materials = properties['materials'].keys()
        shapes = properties['shapes'].keys()
        labels = []
        for z in sizes:
            for c in colors:
                for m in materials:
                    for s in shapes:
                        labels.append('%s_%s_%s_%s' % (z, c, m, s))
    print(len(labels))
    print(json.dumps(labels))
    return labels

if __name__ == '__main__':
    """
    for i in range(250+1):
        idx = str(i).zfill(6)
        image_path = '/media/drive/Jiaying/clevr-dataset-gen/output/images/CLEVR_new_%s.png' % (idx)
        scene_path = '/media/drive/Jiaying/clevr-dataset-gen/output/scenes/CLEVR_new_%s.json' % (idx)
        output_dir = '/media/drive/Jiaying/clevr-dataset-gen/output/annotations'
        output_path = write_xml(image_path, scene_path, output_dir)
    """

    generate_all_class_label()
