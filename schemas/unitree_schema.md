# UniTree Schema

UniTree is a five-tuple T = (V, E, F, B, R).

## Function Node (F)

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier |
| name | string | Function name |
| module | string | Owning module |
| params | list | Parameter list |
| priority | float | Execution priority |
| scope | float | Fault-impact scope |

## Code-Block Node (B)

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier |
| type | enum | CONDITION, LOOP, COMPUTE, IO, EXCEPTION, HANDLER, RESOURCE, RETURN |
| desc | string | Logical description |
| parent | string | Parent node identifier |
| threshold | float | Execution-time threshold |

## Edge Types (R)

| Type | Description |
|------|-------------|
| SEQUENCE | Sequential flow |
| CONDITION | Conditional branch |
| LOOP | Loop back-edge |
| EXCEPTION | Exception propagation |
| PARAMETER | Inter-procedural data flow |
| ASYNC | Async/await relationship |

## Serialization

UniTree is serialized with Protobuf 3.20.3; see `unitree.proto`.
