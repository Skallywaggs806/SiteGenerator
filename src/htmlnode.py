


class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
        self.tag == other.tag and
        self.value == other.value and
        self.children == other.children and
        self.props == other.props
    )

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
        # This method should be implemented in subclasses
        # to convert the node to HTML string

    def props_to_html(self):
        # Convert props dictionary to HTML attributes
        if self.props:
            return ' '.join(f'{key}="{value}"' for key, value in self.props.items())
        return ''

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"