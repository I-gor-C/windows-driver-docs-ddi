# 1394.h header


This header is used by IEEE. For more information, see
- [IEEE](../_IEEE/index.md)

1394.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [ADDRESS_FIFO structure](ns-1394--address-fifo.md) | The ADDRESS_FIFO structure is an entry in a singly-linked list of MDLs used by the REQUEST_ALLOCATE_ADDRESS_RANGE IEEE 1394 bus request. |
| [ADDRESS_OFFSET structure](ns-1394--address-offset.md) | The ADDRESS_OFFSET structure specifies the 48-bit address within a device's IEEE 1394 address space. |
| [ADDRESS_RANGE structure](ns-1394--address-range.md) | The ADDRESS_RANGE structure describes a range in a IEEE 1394 device's address space. |
| [BUS_RESET_DATA structure](ns-1394--bus-reset-data.md) | The BUS_RESET_DATA structure specifies the context for the extended bus reset notification routine. |
| [CONFIG_ROM structure](ns-1394--config-rom.md) | The CONFIG_ROM structure is used to contain the first 24 bytes of an IEEE 1394 device's configuration ROM. |
| [CYCLE_TIME structure](ns-1394--cycle-time.md) | The CYCLE_TIME structure contains the IEEE 1394 isochronous cycle time. |
| [GET_LOCAL_HOST_INFO1 structure](ns-1394--get-local-host-info1.md) | The GET_LOCAL_HOST_INFO1 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel GET_HOST_UNIQUE_ID. |
| [GET_LOCAL_HOST_INFO2 structure](ns-1394--get-local-host-info2.md) | The GET_LOCAL_HOST_INFO2 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel GET_HOST_CAPABILITIES. |
| [GET_LOCAL_HOST_INFO3 structure](ns-1394--get-local-host-info3.md) | The GET_LOCAL_HOST_INFO3 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel = GET_POWER_SUPPLIED. |
| [GET_LOCAL_HOST_INFO4 structure](ns-1394--get-local-host-info4.md) | The GET_LOCAL_HOST_INFO4 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel = GET_PHYS_ADDR_ROUTINE. |
| [GET_LOCAL_HOST_INFO5 structure](ns-1394--get-local-host-info5.md) | The GET_LOCAL_HOST_INFO5 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel = GET_HOST_CONFIG_ROM. |
| [GET_LOCAL_HOST_INFO6 structure](ns-1394--get-local-host-info6.md) | The GET_LOCAL_HOST_INFO6 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request using u.GetLocalHostInformation.nLevel = GET_HOST_CSR_CONTENTS. |
| [GET_LOCAL_HOST_INFO8 structure](ns-1394--get-local-host-info8.md) | The GET_LOCAL_HOST_INFO8 structure contains the data returned by a REQUEST_GET_LOCAL_HOST_INFO request with u.GetLocalHostInformation.nLevel set to GET_HOST_DDI_VERSION. |
| [IO_ADDRESS structure](ns-1394--io-address.md) | The IO_ADDRESS structure specifies the 1394 64-bit destination address for read, write and lock operations. |
| [IRB structure](ns-1394--irb.md) | Drivers use this structure to pass most requests to IEEE 1394 bus driver. |
| [IRB_RECEIVE_PHY_PACKETS structure](ns-1394--irb-receive-phy-packets.md) | This structure contains the fields necessary to carry out a ReceivePhyPackets request. |
| [IRB_REQ_ALLOCATE_ADDRESS_RANGE structure](ns-1394--irb-req-allocate-address-range.md) | This structure contains the fields necessary for the 1394 stack to carry out a request to allocate an address range. |
| [IRB_REQ_ASYNC_LOCK structure](ns-1394--irb-req-async-lock.md) | This structure contains the fields necessary for the 1394 stack to carry out an asychronous lock request. |
| [IRB_REQ_ASYNC_READ structure](ns-1394--irb-req-async-read.md) | This structure contains the fields necessary for the 1394 stack to carry out an asynchronous read request. |
| [IRB_REQ_ASYNC_STREAM structure](ns-1394--irb-req-async-stream.md) | This structure contains the fields necessary for the 1394 bus driver to carry out an asynchronous write request. |
| [IRB_REQ_ASYNC_WRITE structure](ns-1394--irb-req-async-write.md) | This structure contains the fields necessary for the 1394 stack to carry out an asynchronous write request. |
| [IRB_REQ_BUS_RESET structure](ns-1394--irb-req-bus-reset.md) | This structure contains the fields necessary for the 1394 bus driver to create a bus reset request. |
| [IRB_REQ_BUS_RESET_NOTIFICATION structure](ns-1394--irb-req-bus-reset-notification.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a bus reset notification request. |
| [IRB_REQ_CONTROL structure](ns-1394--irb-req-control.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a control request. |
| [IRB_REQ_FREE_ADDRESS_RANGE structure](ns-1394--irb-req-free-address-range.md) | This structure contains the fields necessary for the 1394 stack to carry out a free address range reqeust. |
| [IRB_REQ_GET_1394_ADDRESS_FROM_DEVICE_OBJECT structure](ns-1394--irb-req-get-1394-address-from-device-object.md) | This structure contains the fields necessary to carry out a Get1394AddressFromDeviceObject request. |
| [IRB_REQ_GET_CONFIGURATION_INFORMATION structure](ns-1394--irb-req-get-configuration-information.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a GetConfigurationInformation request. |
| [IRB_REQ_GET_CONFIG_ROM structure](ns-1394--irb-req-get-config-rom.md) | This structure contains the fields necessary for the bus driver to carry out a GetConfigRom request. |
| [IRB_REQ_GET_GENERATION_COUNT structure](ns-1394--irb-req-get-generation-count.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a GetGenerationCount request. |
| [IRB_REQ_GET_LOCAL_HOST_INFORMATION structure](ns-1394--irb-req-get-local-host-information.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a GetLocalHostInformation request. |
| [IRB_REQ_GET_MAX_SPEED_BETWEEN_DEVICES structure](ns-1394--irb-req-get-max-speed-between-devices.md) | This structure contains the fields necessary in order for the Bus driver to carry out a GetMaxSpeedBetweenDevices request. |
| [IRB_REQ_GET_SPEED_TOPOLOGY_MAPS structure](ns-1394--irb-req-get-speed-topology-maps.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a GetSpeedTopologyMaps request. |
| [IRB_REQ_ISOCH_ALLOCATE_BANDWIDTH structure](ns-1394--irb-req-isoch-allocate-bandwidth.md) | This structure contains the fields necessary in order for the Bus driver to carry out an IsochAllocateBandwidth request. |
| [IRB_REQ_ISOCH_ALLOCATE_CHANNEL structure](ns-1394--irb-req-isoch-allocate-channel.md) | This structure contains the fields necessary in order for the 1394 bus driver to carry out an IsochAllocateChannel request. |
| [IRB_REQ_ISOCH_ALLOCATE_RESOURCES_W2K structure](ns-1394--irb-req-isoch-allocate-resources-w2k.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a IsochAllocateResources request. |
| [IRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP structure](ns-1394--irb-req-isoch-allocate-resources-wxp.md) | This structure contains the fields necessary for the 1394 bus driver to carry out a IsochAllocateResources request. |
| [IRB_REQ_ISOCH_ATTACH_BUFFERS structure](ns-1394--irb-req-isoch-attach-buffers.md) | This structure contains the fields required for the 1394 bus driver to carry out a IsochAttachBuffers request. |
| [IRB_REQ_ISOCH_DETACH_BUFFERS structure](ns-1394--irb-req-isoch-detach-buffers.md) | This structure contains the fields required to carry out a IsochDetachBuffers request. |
| [IRB_REQ_ISOCH_FREE_BANDWIDTH structure](ns-1394--irb-req-isoch-free-bandwidth.md) | This structure contains the fields necessary in order for the Bus driver to carry out an IsochFreeBandwidth request. |
| [IRB_REQ_ISOCH_FREE_CHANNEL structure](ns-1394--irb-req-isoch-free-channel.md) | This structure contains the fields required to carry out a IsochFreeChannel request. |
| [IRB_REQ_ISOCH_FREE_RESOURCES structure](ns-1394--irb-req-isoch-free-resources.md) | This structure contains the fields necessary to carry out a IsochFreeResources request. |
| [IRB_REQ_ISOCH_LISTEN structure](ns-1394--irb-req-isoch-listen.md) | This structure contains the fields necessary to carry out a ReqIsochListen request. |
| [IRB_REQ_ISOCH_MODIFY_STREAM_PROPERTIES structure](ns-1394--irb-req-isoch-modify-stream-properties.md) | This structure contains the fields necessary for the Bus driver to carry out an IsochModifyStreamProperties request. |
| [IRB_REQ_ISOCH_QUERY_CURRENT_CYCLE_TIME structure](ns-1394--irb-req-isoch-query-current-cycle-time.md) | This structure contains the fields necessary for the Bus driver to carry out an IsochQueryCurrentCycleTime request. |
| [IRB_REQ_ISOCH_QUERY_RESOURCES structure](ns-1394--irb-req-isoch-query-resources.md) | This structure contains the fields necessary to carry out a IsochQueryResources request. |
| [IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH structure](ns-1394--irb-req-isoch-set-channel-bandwidth.md) | This structure contains the fields necessary for the Bus driver to carry out an IsochSetChannelBandwidth request. |
| [IRB_REQ_ISOCH_STOP structure](ns-1394--irb-req-isoch-stop.md) | This structure contains the field necessary to carry out a IsochStop request. |
| [IRB_REQ_ISOCH_TALK structure](ns-1394--irb-req-isoch-talk.md) | This structure contains the field necessary to carry out a IsochTalk request. |
| [IRB_REQ_SEND_PHY_CONFIGURATION_PACKET structure](ns-1394--irb-req-send-phy-configuration-packet.md) | This structure contains the fields necessary to carry out a SendPhyConfigurationPacket request. |
| [IRB_REQ_SEND_PHY_PACKET structure](ns-1394--irb-req-send-phy-packet.md) | This structure contains the fields necessary to carry out a SendPhyPacket request. |
| [IRB_REQ_SET_DEVICE_XMIT_PROPERTIES structure](ns-1394--irb-req-set-device-xmit-properties.md) | This structure contains the fields necessary to carry out a SetDeviceXmitProperties request. |
| [IRB_REQ_SET_LOCAL_HOST_PROPERTIES structure](ns-1394--irb-req-set-local-host-properties.md) | This structure contains the fields required to carry out a SetLocalHostProperties request. |
| [ISOCH_DESCRIPTOR structure](ns-1394--isoch-descriptor.md) | The ISOCH_DESCRIPTOR structure describes a buffer to be attached or detailed from a resource handle, using the REQUEST_ISOCH_ATTACH_BUFFERS and REQUEST_ISOCH_DETACH_BUFFERS requests. |
| [NODE_ADDRESS structure](ns-1394--node-address.md) | The NODE_ADDRESS structure specifies the 10-bit bus number and 6-bit node number that serve as the node address for a 1394 node. |
| [PHY_CONFIGURATION_PACKET structure](ns-1394--phy-configuration-packet.md) | The PHY_CONFIGURATION_PACKET structure contains a raw PHY configuration packet. |
| [SELF_ID structure](ns-1394--self-id.md) | The SELF_ID structure contains a raw packet zero self-ID packet. See the IEEE 1394 Trade Association specification website for details. |
| [SELF_ID_MORE structure](ns-1394--self-id-more.md) | The SELF_ID_MORE structure contains a raw packet one, two, or three self-ID packet. See the IEEE 1394 specification for details. |
| [SET_LOCAL_HOST_PROPS2 structure](ns-1394--set-local-host-props2.md) | SET_LOCAL_HOST_PROPS2 sets a lower bound on the value the bus will use for its gap count. |
| [SET_LOCAL_HOST_PROPS3 structure](ns-1394--set-local-host-props3.md) | SET_LOCAL_HOST_PROPS3 contains the data necessary for defining or identifying one or more unit directories in the Configuration ROM of a 1394 Host Controller. |
| [SPEED_MAP structure](ns-1394--speed-map.md) | The SPEED_MAP structure is stores a IEEE 1394 bus speed map. |
| [TEXTUAL_LEAF structure](ns-1394--textual-leaf.md) | The TEXTUAL_LEAF structure describes the device description that can be stored in the Configuration ROM of devices that satisfy the PC 98 or PC 99 specifications. |
| [TOPOLOGY_MAP structure](ns-1394--topology-map.md) | The TOPOLOGY_MAP structure is used to store an IEEE 1394 bus topology map. The relations between devices are found in the port members of the entries in TOP_Self_ID_Array. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_1394_CLASS IOCTL](ni-1394-ioctl-1394-class.md) | An IEEE 1394 driver uses the IRP_MJ_INTERNAL_DEVICE_CONTROL IRP, with IoControlCode IOCTL_1394_CLASS, to communicate with the bus driver. The driver has access to all operations provided by the IEEE 1394 bus and its host controller through this request. |
