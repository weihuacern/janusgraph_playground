## JanusGraph Playground
https://github.com/JanusGraph/janusgraph
```bash
docker-compose -f ./docker-compose.yml up -d
```

### graphexp
An simple visulization tool for gremlin
```
https://github.com/bricaud/graphexp
https://github.com/erandal/janusgraph-env
http://192.168.7.143:8183
```

### JanusGraph
#### Gremlin server
```
GraphSONMessageSerializerV3d0
```

### Storage DB
#### Scylla
#### Cassandra

### Indexing DB
#### Elasticsearch
##### DEBUG
- 1, max\_map\_count
```
sysctl -w vm.max_map_count=262144
https://elk-docker.readthedocs.io/#es-not-starting-max-map-count
https://github.com/spujadas/elk-docker/issues/89
https://www.kernel.org/doc/Documentation/sysctl/vm.txt
```

- 2, Failed to create node environment
```
chmod 777 data/elasticsearch/data/
https://github.com/elastic/elasticsearch-docker/issues/21
```

### Client
#### Python
```
pip3.6 install gremlinpython
pip3.6 install aiogremlin
https://aiogremlin.readthedocs.io/en/latest/
```
