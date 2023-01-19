# Traces

This repo is simply for showing what data we are dealing with for finding the points of divergence/convergence of 2 executions. To be more precise, we have function call traces (in the directory traces) and program specification(in the directory progSpec) of the trace. 

### Function Call Traces
Function call traces are shown in the following format.
```
main
printf
/printf
/main
```
One line represents either entering into the function, or exitting out of the function.
The character '/' means exitting from the function. For instance, "/printf" means exitting out of "printf". If the character '/' does not exist in the line, that means entering into the function (e.g. "main" means entering into the function "main").

These are captured through the use of Intel Pin (I believe it's staic binary instrumentation, but I need to check), and some functions do not use the instruction "ret" to return (they normally use "jump"s), in that case the return of the function is sometimes not recorded (we figure out the detail by looking at program specification in this case). 

### Program Specifications
Program Spefications are shown as the set of functions, where the entry point of the execution is "main". Each function, a simplified control flow graph of the function, has a set of nodes and edges, with one entry point and one return call. In this implementation, it also has a function call as a type of node (in addition to entry point and return call), with the label (basically telling you which function it was, for instance, printf). 

Given that, the format of the JSON file will be the following
```
{
    {
    "function name": "main", 
    "nodes": [ 
        {
        "id": "a",
        "type": "entryPoint"
        },
        {
        "id": "b",
        "type": "funcCall",
        "label": "F"
        },
        {
        "id": "c",
        "type": "return"
        }
    ], 
    "edges": [
        {
        "src": "a",
        "dst": "b"
        },
        {
        "src": "b",
        "dst": "c"
        }   
    ]
    },
    {
    "function name": "F",
    "nodes": [ 
        {
        "id": "d",
        "type": "entryPoint"
        },
        {
        "id": "e",
        "type": "return"
        }
    ], 
    "edges": [
        {
        "src": "d",
        "dst": "e"
        }   
    ]
    }
}
```

"function name" is literally function name. 
nodes have id, which has to be unique to each node, and label for funcCall nodes, label has to be one of the function names, and multiple nodes can have the same label. "type" is explained above.
edges have source and destination, because the graphs are directed.

Hope this texts clarify! For questions, ask at ynakamu1@depaul.edu.

