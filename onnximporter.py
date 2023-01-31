import onnx
from onnx import helper

# Create transpose and reshape nodes
transpose_node = helper.make_node('Transpose', inputs=['concat_output'], outputs=['transposed_output'], perm=[0, 2, 3, 1])
reshape_node = helper.make_node('Reshape', inputs=['transposed_output'], outputs=['reshaped_output'], shape=[-1, 1, 28, 28])

# Add nodes to the model
model = onnx.load('Fastkt.onnx')
model.graph.sequential.append([transpose_node, reshape_node])

# Save the model
onnx.save(model, 'updated_model.onnx')