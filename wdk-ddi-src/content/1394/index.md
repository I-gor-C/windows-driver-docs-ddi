---
UID: NA:
---

# 1394.h header

## -description

This header is used by IEEE. For more information, see
- [IEEE](../_IEEE/index.md)

1394.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_ADDRESS_FIFO structure](ns-1394-_address_fifo.md) | The ADDRESS_FIFO structure is an entry in a singly-linked list of MDLs used by the REQUEST_ALLOCATE_ADDRESS_RANGE IEEE 1394 bus request. |
| [_ADDRESS_OFFSET structure](ns-1394-_address_offset.md) | The ADDRESS_OFFSET structure specifies the 48-bit address within a device's IEEE 1394 address space. |
| [_ADDRESS_RANGE structure](ns-1394-_address_range.md) | The ADDRESS_RANGE structure describes a range in a IEEE 1394 device's address space. |
| [_BUS_RESET_DATA structure](ns-1394-_bus_reset_data.md) | The BUS_RESET_DATA structure specifies the context for the extended bus reset notification routine. |
| [_CONFIG_ROM structure](ns-1394-_config_rom.md) | The CONFIG_ROM structure is used to contain the first 24 bytes of an IEEE 1394 device's configuration ROM. |
| [_CYCLE_TIME structure](ns-1394-_cycle_time.md) | The CYCLE_TIME structure contains the IEEE 1394 isochronous cycle time. |
| [_GET_LOCAL_HOST_INFO1 structure](ns-1394-_get_local_host_info1.md) | The GET_LOCAL_HOST_INFO1 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel GET_HOST_UNIQUE_ID. |
| [_GET_LOCAL_HOST_INFO2 structure](ns-1394-_get_local_host_info2.md) | The GET_LOCAL_HOST_INFO2 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel GET_HOST_CAPABILITIES. |
| [_GET_LOCAL_HOST_INFO3 structure](ns-1394-_get_local_host_info3.md) | The GET_LOCAL_HOST_INFO3 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel = GET_POWER_SUPPLIED. |
| [_GET_LOCAL_HOST_INFO4 structure](ns-1394-_get_local_host_info4.md) | The GET_LOCAL_HOST_INFO4 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel = GET_PHYS_ADDR_ROUTINE. |
| [_GET_LOCAL_HOST_INFO5 structure](ns-1394-_get_local_host_info5.md) | The GET_LOCAL_HOST_INFO5 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel = GET_HOST_CONFIG_ROM. |
| [_GET_LOCAL_HOST_INFO6 structure](ns-1394-_get_local_host_info6.md) | The GET_LOCAL_HOST_INFO6 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel = GET_HOST_CSR_CONTENTS. |
| [_GET_LOCAL_HOST_INFO8 structure](ns-1394-_get_local_host_info8.md) | The GET_LOCAL_HOST_INFO8 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request with u.GetLocalHostInformation.nLevel set to GET_HOST_DDI_VERSION. |
| [_IO_ADDRESS structure](ns-1394-_io_address.md) | The IO_ADDRESS structure specifies the 1394 64-bit destination address for read, write and lock operations. |
| [_IRB structure](ns-1394-_irb.md) | Drivers use this structure to pass most requests to IEEE 1394 bus driver. |
| [_IRB_RECEIVE_PHY_PACKETS structure](ns-1394-_irb_receive_phy_packets.md) | This structure contains the fields necessary to carry out a ReceivePhyPackets request. |
| [_IRB_REQ_ALLOCATE_ADDRESS_RANGE structure](ns-1394-_irb_req_allocate_address_range.md) | This structure contains the fields necessary for the 1394 stack to carry out a request to allocate an address range. |
| [_IRB_REQ_ASYNC_LOCK structure](ns-1394-_irb_req_async_lock.md) | This structure contains the fields necessary for the 1394 stack to carry out an asychronous lock request. |
| [_IRB_REQ_ASYNC_READ structure](ns-1394-_irb_req_async_read.md) | This structure contains the fields necessary for the 1394 stack to carry out an asynchronous read request. |
| [_IRB_REQ_ASYNC_STREAM structure](ns-1394-_irb_req_async_stream.md) | This structure contains the fields necessary for the 1394 bus driver to carry out an asynchronous write request. |
| [_IRB_REQ_ASYNC_WRITE structure](ns-1394-_irb_req_async_write.md) | This structure contains the fields necessary for the 1394 stack to carry out an asynchronous write request. |
| [_IRB_REQ_BUS_RESET structure](ns-1394-_irb_req_bus_reset.md) | This structure contains the fields necessary for the 1394 bus driver to create a bus reset request. |
| [_IRB_REQ_BUS_RESET_NOTIFICATION structure](ns-1394-_irb_req_bus_reset_notification.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a bus reset notification request. |
| [_IRB_REQ_CONTROL structure](ns-1394-_irb_req_control.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a control request. |
| [_IRB_REQ_FREE_ADDRESS_RANGE structure](ns-1394-_irb_req_free_address_range.md) | This structure contains the fields necessary for the 1394 stack to carry out a free address range reqeust. |
| [_IRB_REQ_GET_1394_ADDRESS_FROM_DEVICE_OBJECT structure](ns-1394-_irb_req_get_1394_address_from_device_object.md) | This structure contains the fields necessary to carry out a Get1394AddressFromDeviceObject request. |
| [_IRB_REQ_GET_CONFIGURATION_INFORMATION structure](ns-1394-_irb_req_get_configuration_information.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a GetConfigurationInformation request. |
| [_IRB_REQ_GET_CONFIG_ROM structure](ns-1394-_irb_req_get_config_rom.md) | This structure contains the fields necessary for the bus driver to carry out a GetConfigRom request. |
| [_IRB_REQ_GET_GENERATION_COUNT structure](ns-1394-_irb_req_get_generation_count.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a GetGenerationCount request. |
| [_IRB_REQ_GET_LOCAL_HOST_INFORMATION structure](ns-1394-_irb_req_get_local_host_information.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a GetLocalHostInformation request. |
| [_IRB_REQ_GET_MAX_SPEED_BETWEEN_DEVICES structure](ns-1394-_irb_req_get_max_speed_between_devices.md) | This structure contains the fields necessary in order for the Bus driver to carry out a GetMaxSpeedBetweenDevices request. |
| [_IRB_REQ_GET_SPEED_TOPOLOGY_MAPS structure](ns-1394-_irb_req_get_speed_topology_maps.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a GetSpeedTopologyMaps request. |
| [_IRB_REQ_ISOCH_ALLOCATE_BANDWIDTH structure](ns-1394-_irb_req_isoch_allocate_bandwidth.md) | This structure contains the fields necessary in order for the Bus driver to carry out an IsochAllocateBandwidth request. |
| [_IRB_REQ_ISOCH_ALLOCATE_CHANNEL structure](ns-1394-_irb_req_isoch_allocate_channel.md) | This structure contains the fields necessary in order for the 1394 bus driver to carry out an IsochAllocateChannel request. |
| [_IRB_REQ_ISOCH_ALLOCATE_RESOURCES_W2K structure](ns-1394-_irb_req_isoch_allocate_resources_w2k.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a IsochAllocateResources request. |
| [_IRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP structure](ns-1394-_irb_req_isoch_allocate_resources_wxp.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a IsochAllocateResources request. |
| [_IRB_REQ_ISOCH_ATTACH_BUFFERS structure](ns-1394-_irb_req_isoch_attach_buffers.md) | This structure contains the fields required for the 1394 bus driver to carry out a IsochAttachBuffers request. |
| [_IRB_REQ_ISOCH_DETACH_BUFFERS structure](ns-1394-_irb_req_isoch_detach_buffers.md) | This structure contains the fields required to carry out a IsochDetachBuffers request. |
| [_IRB_REQ_ISOCH_FREE_BANDWIDTH structure](ns-1394-_irb_req_isoch_free_bandwidth.md) | This structure contains the fields necessary in order for the Bus driver to carry out an IsochFreeBandwidth request. |
| [_IRB_REQ_ISOCH_FREE_CHANNEL structure](ns-1394-_irb_req_isoch_free_channel.md) | This structure contains the fields required to carry out a IsochFreeChannel request. |
| [_IRB_REQ_ISOCH_FREE_RESOURCES structure](ns-1394-_irb_req_isoch_free_resources.md) | This structure contains the fields necessary to carry out a IsochFreeResources request. |
| [_IRB_REQ_ISOCH_LISTEN structure](ns-1394-_irb_req_isoch_listen.md) | This structure contains the fields necessary to carry out a ReqIsochListen request. |
| [_IRB_REQ_ISOCH_MODIFY_STREAM_PROPERTIES structure](ns-1394-_irb_req_isoch_modify_stream_properties.md) | This structure contains the fields necessary for the Bus driver to carry out an IsochModifyStreamProperties request. |
| [_IRB_REQ_ISOCH_QUERY_CURRENT_CYCLE_TIME structure](ns-1394-_irb_req_isoch_query_current_cycle_time.md) | This structure contains the fields necessary for the Bus driver to carry out an IsochQueryCurrentCycleTime request. |
| [_IRB_REQ_ISOCH_QUERY_RESOURCES structure](ns-1394-_irb_req_isoch_query_resources.md) | This structure contains the fields necessary to carry out a IsochQueryResources request. |
| [_IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH structure](ns-1394-_irb_req_isoch_set_channel_bandwidth.md) | This structure contains the fields necessary for the Bus driver to carry out an IsochSetChannelBandwidth request. |
| [_IRB_REQ_ISOCH_STOP structure](ns-1394-_irb_req_isoch_stop.md) | This structure contains the field necessary to carry out a IsochStop request. |
| [_IRB_REQ_ISOCH_TALK structure](ns-1394-_irb_req_isoch_talk.md) | This structure contains the field necessary to carry out a IsochTalk request. |
| [_IRB_REQ_SEND_PHY_CONFIGURATION_PACKET structure](ns-1394-_irb_req_send_phy_configuration_packet.md) | This structure contains the fields necessary to carry out a SendPhyConfigurationPacket request. |
| [_IRB_REQ_SEND_PHY_PACKET structure](ns-1394-_irb_req_send_phy_packet.md) | This structure contains the fields necessary to carry out a SendPhyPacket request. |
| [_IRB_REQ_SET_DEVICE_XMIT_PROPERTIES structure](ns-1394-_irb_req_set_device_xmit_properties.md) | This structure contains the fields necessary to carry out a SetDeviceXmitProperties request. |
| [_IRB_REQ_SET_LOCAL_HOST_PROPERTIES structure](ns-1394-_irb_req_set_local_host_properties.md) | This structure contains the fields required to carry out a SetLocalHostProperties request. |
| [_ISOCH_DESCRIPTOR structure](ns-1394-_isoch_descriptor.md) | The ISOCH_DESCRIPTOR structure describes a buffer to be attached or detailed from a resource handle, using the REQUEST_ISOCH_ATTACH_BUFFERS and REQUEST_ISOCH_DETACH_BUFFERS requests. |
| [_NODE_ADDRESS structure](ns-1394-_node_address.md) | The NODE_ADDRESS structure specifies the 10-bit bus number and 6-bit node number that serve as the node address for a 1394 node. |
| [_PHY_CONFIGURATION_PACKET structure](ns-1394-_phy_configuration_packet.md) | The PHY_CONFIGURATION_PACKET structure contains a raw PHY configuration packet. |
| [_SELF_ID structure](ns-1394-_self_id.md) | The SELF_ID structure contains a raw packet zero self-ID packet. See the IEEE 1394 Trade Association specification website for details. |
| [_SELF_ID_MORE structure](ns-1394-_self_id_more.md) | The SELF_ID_MORE structure contains a raw packet one, two, or three self-ID packet. See the IEEE 1394 specification for details. |
| [_SET_LOCAL_HOST_PROPS2 structure](ns-1394-_set_local_host_props2.md) | SET_LOCAL_HOST_PROPS2 sets a lower bound on the value the bus will use for its gap count. |
| [_SET_LOCAL_HOST_PROPS3 structure](ns-1394-_set_local_host_props3.md) | SET_LOCAL_HOST_PROPS3 contains the data necessary for defining or identifying one or more unit directories in the Configuration ROM of a 1394 Host Controller. |
| [_SPEED_MAP structure](ns-1394-_speed_map.md) | The SPEED_MAP structure is stores a IEEE 1394 bus speed map. |
| [_TEXTUAL_LEAF structure](ns-1394-_textual_leaf.md) | The TEXTUAL_LEAF structure describes the device description that can be stored in the Configuration ROM of devices that satisfy the PC 98 or PC 99 specifications. |
| [_TOPOLOGY_MAP structure](ns-1394-_topology_map.md) | The TOPOLOGY_MAP structure is used to store an IEEE 1394 bus topology map. The relations between devices are found in the port members of the entries in TOP_Self_ID_Array. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_1394_CLASS IOCTL](ni-1394-ioctl_1394_class.md) | An IEEE 1394 driver uses the IRP_MJ_INTERNAL_DEVICE_CONTROL IRP, with IoControlCode IOCTL_1394_CLASS, to communicate with the bus driver. The driver has access to all operations provided by the IEEE 1394 bus and its host controller through this request. |
