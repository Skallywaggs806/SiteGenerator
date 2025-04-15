


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
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        # Check if value is None or empty
        if not self.value:
          raise ValueError("LeafNode must have a value")
        
        # If tag is None, return raw value
        if self.tag is None:
            return self.value
        
        # Otherwise, render as HTML tag
        props_str = self.props_to_html()
        if props_str:
            return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        self.children = children
    
    def to_html(self):
        # Check if children is empty
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        #Check if tag is None
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        # Render the opening tag
        props_str = self.props_to_html()
        if props_str:
            opening_tag = f"<{self.tag} {props_str}>"
        else:
            opening_tag = f"<{self.tag}>"
        
        # Render the children
        children_html = ''.join(child.to_html() for child in self.children)
        
        # Render the closing tag
        closing_tag = f"</{self.tag}>"
        
        return f"{opening_tag}{children_html}{closing_tag}"


