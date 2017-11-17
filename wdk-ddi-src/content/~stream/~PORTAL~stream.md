# Declarations in the stream technology
This technology  contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [tagKS_DATARANGE_MPEG2TS_AVC structure](..\avcstrm\ns-avcstrm-tagks-datarange-mpeg2ts-avc.md) | The KS_DATARANGE_MPEG2TS_AVC structure stores a range of AV/C MPEG2 formats. |
| [tagKS_DATARANGE_DVVIDEO structure](..\avcstrm\ns-avcstrm-tagks-datarange-dvvideo.md) | The KS_DATARANGE_DV_AVC structure stores a range of digital video formats. |
| [AVCSTRM_OPEN_STRUCT structure](..\avcstrm\ns-avcstrm--avcstrm-open-struct.md) | The AVCSTRM_OPEN_STRUCT structure describes a data stream to be opened. |
| [tagKS_DATARANGE_DV_AVC structure](..\avcstrm\ns-avcstrm-tagks-datarange-dv-avc.md) | The KS_DATARANGE_DV_AVC structure stores a range of AV/C digital video formats. |
| [AVCSTRM_FORMAT_INFO structure](..\avcstrm\ns-avcstrm--avcstrm-format-info.md) | The AVCSTRM_FORMAT_INFO structure is used to describe a data stream. |
| [CIP_HDR2_FDF structure](..\avcstrm\ns-avcstrm--cip-hdr2-fdf.md) | The CIP_HDR2_FDF structure describes the second quadlet of a CIP header pair. |
| [CIP_HDR1 structure](..\avcstrm\ns-avcstrm--cip-hdr1.md) | The CIP_HDR1 structure describes the generic data structure of the two quadlet CIP headers (first quadlet of the pair). |
| [tagKS_DATAFORMAT_DV_AVC structure](..\avcstrm\ns-avcstrm-tagks-dataformat-dv-avc.md) | The KS_DATAFORMAT_DV_AVC structure stores the data format for an AV/C digital video connection. |
| [CIP_HDR2_SYT structure](..\avcstrm\ns-avcstrm--cip-hdr2-syt.md) | The CIP_HDR2_SYT structure describes the second quadlet of a CIP header pair for a DV format stream. |
| [DVINFO structure](..\avcstrm\ns-avcstrm--dvinfo.md) | The DVINFO structure describes a DV stream format including its default streaming source information and stream control information. |
| [AVC_STREAM_REQUEST_BLOCK structure](..\avcstrm\ns-avcstrm--avc-stream-request-block.md) | The AVC_STREAM_REQUEST_BLOCK structure describes an AV/C streaming request to be processed by avcstrm.sys. |
| [AVCSTRM_BUFFER_STRUCT structure](..\avcstrm\ns-avcstrm--avcstrm-buffer-struct.md) | The AVCSTRM_BUFFER_STRUCT structure describes a buffer to be submitted to avcstrm.sys for read or write operations. |
| [tagKS_DATAFORMAT_MPEG2TS_AVC structure](..\avcstrm\ns-avcstrm-tagks-dataformat-mpeg2ts-avc.md) | The KS_DATAFORMAT_MPEG2TS_AVC structure stores the data format for an AV/C MPEG2 connection. |
| [CIP_HDR2_MPEGTS structure](..\avcstrm\ns-avcstrm--cip-hdr2-mpegts.md) | The CIP_HDR2_MPEGTS structure describes the second quadlet of a CIP header pair for an MPEGTS format stream. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [AVCSTRM_FORMAT enumeration](..\avcstrm\ne-avcstrm--avcstrm-format.md) | The AVCSTRM_FUNCTION enumeration defines the AV/C subunit stream formats supported by avcstrm.sys. |
| [AVCSTRM_FUNCTION enumeration](..\avcstrm\ne-avcstrm--avcstrm-function.md) | The AVCSTRM_FUNCTION enumeration defines the functionality exposed by the avcstrm.sys driver. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [BdaInitFilter function](..\bdasup\nf-bdasup-bdainitfilter.md) | The BdaInitFilter function initializes the BDA filter context associated with a filter instance. |
| [BdaGetChangeState function](..\bdasup\nf-bdasup-bdagetchangestate.md) | The BdaGetChangeState function returns the current change state of BDA topology. |
| [BdaCheckChanges function](..\bdasup\nf-bdasup-bdacheckchanges.md) | The BdaCheckChanges function verifies a new set of BDA topology changes before they are committed. |
| [BdaCreateFilterFactoryEx function](..\bdasup\nf-bdasup-bdacreatefilterfactoryex.md) | The BdaCreateFilterFactoryEx function adds the specified filter descriptor as a filter factory to the specified device and associates the filter factory with the specified BDA template topology. |
| [BdaMethodCreatePin function](..\bdasup\nf-bdasup-bdamethodcreatepin.md) | The BdaMethodCreatePin function creates a pin factory. |
| [BdaStartChanges function](..\bdasup\nf-bdasup-bdastartchanges.md) | The BdaStartChanges function initiates the setting of new BDA topology changes. |
| [BdaPropertyNodeProperties function](..\bdasup\nf-bdasup-bdapropertynodeproperties.md) | The BdaPropertyNodeProperties function retrieves a list of properties that a node supports. |
| [BdaCommitChanges function](..\bdasup\nf-bdasup-bdacommitchanges.md) | The BdaCommitChanges function commits the changes to BDA topology that have occurred since the last call to the BdaStartChanges function. |
| [BdaUninitFilter function](..\bdasup\nf-bdasup-bdauninitfilter.md) | The BdaUninitFilter function removes the BDA filter context from the associated filter instance. |
| [BdaPropertyNodeDescriptors function](..\bdasup\nf-bdasup-bdapropertynodedescriptors.md) | The BdaPropertyNodeDescriptors function retrieves a list of nodes in a template topology. |
| [BdaCreateFilterFactory function](..\bdasup\nf-bdasup-bdacreatefilterfactory.md) | The BdaCreateFilterFactory function adds the specified filter descriptor as a filter factory to the specified device and associates the filter factory with the specified BDA template topology. |
| [BdaPropertyGetPinControl function](..\bdasup\nf-bdasup-bdapropertygetpincontrol.md) | The BdaPropertyGetPinControl function retrieves either the identifier or type of a pin. |
| [BdaCreateTopology function](..\bdasup\nf-bdasup-bdacreatetopology.md) | The BdaCreateTopology function creates the topology between two pins. |
| [BdaPropertyGetControllingPinId function](..\bdasup\nf-bdasup-bdapropertygetcontrollingpinid.md) | The BdaPropertyGetControllingPinId function retrieves the identifier of a pin on which to control the properties, methods, and events of a specific node. |
| [BdaPropertyNodeMethods function](..\bdasup\nf-bdasup-bdapropertynodemethods.md) | The BdaPropertyNodeMethods function retrieves a list of methods that a node supports. |
| [BdaPropertyNodeTypes function](..\bdasup\nf-bdasup-bdapropertynodetypes.md) | The BdaPropertyNodeTypes function retrieves a list of node types in a template topology. |
| [BdaPropertyPinTypes function](..\bdasup\nf-bdasup-bdapropertypintypes.md) | The BdaPropertyPinTypes function retrieves a list of pin types in a template topology. |
| [BdaDeletePin function](..\bdasup\nf-bdasup-bdadeletepin.md) | The BdaDeletePin function deletes a pin from the specified filter. |
| [BdaPropertyNodeEvents function](..\bdasup\nf-bdasup-bdapropertynodeevents.md) | The BdaPropertyNodeEvents function retrieves a list of events that a node supports. |
| [BdaValidateNodeProperty function](..\bdasup\nf-bdasup-bdavalidatenodeproperty.md) | The BdaValidateNodeProperty function validates that a node property request is associated with a specific pin. |
| [BdaMethodCreateTopology function](..\bdasup\nf-bdasup-bdamethodcreatetopology.md) | The BdaMethodCreateTopology function creates a template topology between two pins of a filter. |
| [BdaPropertyTemplateConnections function](..\bdasup\nf-bdasup-bdapropertytemplateconnections.md) | The BdaPropertyTemplateConnections function retrieves a list of connections that describe how pin types and node types are connected in a template topology. |
| [BdaCreatePin function](..\bdasup\nf-bdasup-bdacreatepin.md) | The BdaCreatePin function creates a new pin in the specified filter. |
| [BdaMethodDeletePin function](..\bdasup\nf-bdasup-bdamethoddeletepin.md) | The BdaMethodDeletePin function deletes a pin factory. |
| [BdaFilterFactoryUpdateCacheData function](..\bdasup\nf-bdasup-bdafilterfactoryupdatecachedata.md) | The BdaFilterFactoryUpdateCacheData function updates the pin data cache for an instance of a filter. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BDA_PIN_PAIRING structure](..\bdasup\ns-bdasup--bda-pin-pairing.md) | The BDA_PIN_PAIRING structure describes the topology between a pair of input and output pins. |
| [KSM_PIN structure](..\bdasup\ns-bdasup--ksm-pin.md) | The KSM_PIN structure describes a method request to create or delete a pin factory for a filter. |
| [KSM_PIN_PAIR structure](..\bdasup\ns-bdasup--ksm-pin-pair.md) | The KSM_PIN_PAIR structure describes a method request to retrieve the pin pairing structure (BDA_PIN_PAIRING) between a pair of input and output pins. |
| [BDA_FILTER_TEMPLATE structure](..\bdasup\ns-bdasup--bda-filter-template.md) | The BDA_FILTER_TEMPLATE structure describes the template topology for a BDA filter. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BDA_ETHERNET_ADDRESS structure](..\bdatypes\ns-bdatypes--bda-ethernet-address.md) | TBD. |
| [BDA_SCAN_CAPABILTIES structure](..\bdatypes\ns-bdatypes--bda-scan-capabilties.md) | TBD. |
| [BDA_TS_SELECTORINFO structure](..\bdatypes\ns-bdatypes--bda-ts-selectorinfo.md) | TBD. |
| [BDA_WMDRMTUNER_PURCHASEENTITLEMENT structure](..\bdatypes\ns-bdatypes--bda-wmdrmtuner-purchaseentitlement.md) | TBD. |
| [BDA_IPv4_ADDRESS_LIST structure](..\bdatypes\ns-bdatypes--bda-ipv4-address-list.md) | TBD. |
| [BDA_ETHERNET_ADDRESS_LIST structure](..\bdatypes\ns-bdatypes--bda-ethernet-address-list.md) | TBD. |
| [BDA_TS_SELECTORINFO_ISDBS_EXT structure](..\bdatypes\ns-bdatypes--bda-ts-selectorinfo-isdbs-ext.md) | TBD. |
| [BDA_ISDBCAS_RESPONSEDATA structure](..\bdatypes\ns-bdatypes--bda-isdbcas-responsedata.md) | TBD. |
| [BDA_DISEQC_SEND structure](..\bdatypes\ns-bdatypes--bda-diseqc-send.md) | TBD. |
| [BDA_TEMPLATE_CONNECTION structure](..\bdatypes\ns-bdatypes--bda-template-connection.md) | The BDA_TEMPLATE_CONNECTION structure describes the template for a BDA connection in terms of where it begins and ends. |
| [BDA_ISDBCAS_REQUESTHEADER structure](..\bdatypes\ns-bdatypes--bda-isdbcas-requestheader.md) | TBD. |
| [PID_MAP structure](..\bdatypes\ns-bdatypes-pid-map.md) | The PID_MAP structure describes a group of packets in the output stream of a packet identifier (PID) filter. This group consists of packets that are identified with an identical PID and contain particular media content. |
| [BDA_TABLE_SECTION structure](..\bdatypes\ns-bdatypes--bda-table-section.md) | The BDA_TABLE_SECTION structure describes a table section. |
| [BDA_CAS_CHECK_ENTITLEMENTTOKEN structure](..\bdatypes\ns-bdatypes--bda-cas-check-entitlementtoken.md) | TBD. |
| [BDA_CAS_REQUESTTUNERDATA structure](..\bdatypes\ns-bdatypes--bda-cas-requesttunerdata.md) | TBD. |
| [BDA_PROGRAM_PID_LIST structure](..\bdatypes\ns-bdatypes--bda-program-pid-list.md) | The BDA_PROGRAM_PID_LIST structure describes data of a specific program to view. This data consists of packets that are identified with packet identifiers (PID). |
| [BDA_WMDRMTUNER_PIDPROTECTION structure](..\bdatypes\ns-bdatypes--bda-wmdrmtuner-pidprotection.md) | TBD. |
| [BDANODE_DESCRIPTOR structure](..\bdatypes\ns-bdatypes--bdanode-descriptor.md) | The BDANODE_DESCRIPTOR structure describes a BDA node. |
| [BDA_USERACTIVITY_INTERVAL structure](..\bdatypes\ns-bdatypes--bda-useractivity-interval.md) | TBD. |
| [BDA_SIGNAL_TIMEOUTS structure](..\bdatypes\ns-bdatypes--bda-signal-timeouts.md) | TBD. |
| [BDA_TUNER_TUNERSTATE structure](..\bdatypes\ns-bdatypes--bda-tuner-tunerstate.md) | TBD. |
| [BDA_CAS_CLOSE_MMIDIALOG structure](..\bdatypes\ns-bdatypes--bda-cas-close-mmidialog.md) | TBD. |
| [BDA_IPv4_ADDRESS structure](..\bdatypes\ns-bdatypes--bda-ipv4-address.md) | TBD. |
| [BDA_GDDS_DATA structure](..\bdatypes\ns-bdatypes--bda-gdds-data.md) | TBD. |
| [BDA_IPv6_ADDRESS_LIST structure](..\bdatypes\ns-bdatypes--bda-ipv6-address-list.md) | TBD. |
| [BDA_RATING_PINRESET structure](..\bdatypes\ns-bdatypes--bda-rating-pinreset.md) | TBD. |
| [BDA_PID_UNMAP structure](..\bdatypes\ns-bdatypes--bda-pid-unmap.md) | The BDA_PID_UNMAP structure describes packet types to stop filtering from the input stream of a packet identifier (PID) filter. These packet types are identified with PIDs. |
| [BDA_DVBT2_L1_SIGNALLING_DATA structure](..\bdatypes\ns-bdatypes--bda-dvbt2-l1-signalling-data.md) | TBD. |
| [BDA_SCAN_STATE structure](..\bdatypes\ns-bdatypes--bda-scan-state.md) | TBD. |
| [BDA_DISEQC_RESPONSE structure](..\bdatypes\ns-bdatypes--bda-diseqc-response.md) | TBD. |
| [BDA_CAS_CLOSEMMIDATA structure](..\bdatypes\ns-bdatypes--bda-cas-closemmidata.md) | TBD. |
| [BDA_PID_MAP structure](..\bdatypes\ns-bdatypes--bda-pid-map.md) | The BDA_PID_MAP structure describes a type of data to filter out of the input stream of a packet identifier (PID) filter and then pass to a downstream filter. |
| [BDA_SCAN_START structure](..\bdatypes\ns-bdatypes--bda-scan-start.md) | TBD. |
| [BDA_TEMPLATE_PIN_JOINT structure](..\bdatypes\ns-bdatypes--bda-template-pin-joint.md) | The BDA_TEMPLATE_PIN_JOINT structure describes a joint in a template topology. |
| [BDA_TUNER_DIAGNOSTICS structure](..\bdatypes\ns-bdatypes--bda-tuner-diagnostics.md) | TBD. |
| [MPEG2_TRANSPORT_STRIDE structure](..\bdatypes\ns-bdatypes--mpeg2-transport-stride.md) | The MPEG2_TRANSPORT_STRIDE structure describes the format block of the MPEG2 transport stride. |
| [BDA_STRING structure](..\bdatypes\ns-bdatypes--bda-string.md) | TBD. |
| [BDA_WMDRM_STATUS structure](..\bdatypes\ns-bdatypes--bda-wmdrm-status.md) | TBD. |
| [BDA_BUFFER structure](..\bdatypes\ns-bdatypes--bda-buffer.md) | TBD. |
| [BDA_WMDRM_RENEWLICENSE structure](..\bdatypes\ns-bdatypes--bda-wmdrm-renewlicense.md) | TBD. |
| [BDA_CA_MODULE_UI structure](..\bdatypes\ns-bdatypes--bda-ca-module-ui.md) | The BDA_CA_MODULE_UI structure describes the user interface (UI) that conditional access (CA) plugins can display. |
| [BDA_DRM_DRMSTATUS structure](..\bdatypes\ns-bdatypes--bda-drm-drmstatus.md) | TBD. |
| [BDA_IPv6_ADDRESS structure](..\bdatypes\ns-bdatypes--bda-ipv6-address.md) | TBD. |
| [BDA_CAS_OPENMMIDATA structure](..\bdatypes\ns-bdatypes--bda-cas-openmmidata.md) | TBD. |
| [BDA_GDDS_DATATYPE structure](..\bdatypes\ns-bdatypes--bda-gdds-datatype.md) | TBD. |
| [BDA_WMDRM_KEYINFOLIST structure](..\bdatypes\ns-bdatypes--bda-wmdrm-keyinfolist.md) | TBD. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IKsPropertySet::Set method](..\dsound\nf-dsound-ikspropertyset-set.md) | The Set method sets a property identified by a property-set GUID and a property identifier. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [KoDeviceInitialize function](..\kcom\nf-kcom-kodeviceinitialize.md) | The KoDeviceInitialize function adds a kernel COM create-item entry to the specified device object. |
| [KoDriverInitialize function](..\kcom\nf-kcom-kodriverinitialize.md) | The KoDriverInitialize function initializes a driver object to handle the kernel streaming interface. |
| [KoRelease function](..\kcom\nf-kcom-korelease.md) | The KoRelease function decrements the reference count for the calling interface on an object. |
| [KoCreateInstance function](..\kcom\nf-kcom-kocreateinstance.md) | The KoCreateInstance function creates an object of the class with the specified CLSID. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [KSPROPERTY_PIN enumeration](..\ks\ne-ks-ksproperty-pin.md) | TBD. |
| [KSLIST_ENTRY_LOCATION enumeration](..\ks\ne-ks-kslist-entry-location.md) | TBD. |
| [KSPROPERTY_QUALITY enumeration](..\ks\ne-ks-ksproperty-quality.md) | TBD. |
| [KSPROPERTY_GENERAL enumeration](..\ks\ne-ks-ksproperty-general.md) | TBD. |
| [KSSTACK_USE enumeration](..\ks\ne-ks-ksstack-use.md) | TBD. |
| [PKSPIN_DATAFLOW enumeration](..\ks\ne-ks-pkspin-dataflow.md) | An instance of the KSPIN_DATAFLOW enumeration is returned by KSPROPERTY_PIN_DATAFLOW. |
| [KSEVENT_DEVICE enumeration](..\ks\ne-ks-ksevent-device.md) | Specifies event notifications that the driver generates to indicate that a device has been lost or preempted. |
| [KSDEGRADE_STANDARD enumeration](..\ks\ne-ks-ksdegrade-standard.md) | The KSDEGRADE_STANDARD enumeration lists different types of degradation. |
| [KSEVENT_PINCAPS_CHANGENOTIFICATIONS enumeration](..\ks\ne-ks-ksevent-pincaps-changenotifications.md) | TBD. |
| [VARENUM enumeration](..\ks\ne-ks-varenum.md) | TBD. |
| [KSPROPERTY_STREAMALLOCATOR enumeration](..\ks\ne-ks-ksproperty-streamallocator.md) | TBD. |
| [KSMETHOD_STREAMALLOCATOR enumeration](..\ks\ne-ks-ksmethod-streamallocator.md) | TBD. |
| [KSEVENT_VOLUMELIMIT enumeration](..\ks\ne-ks-ksevent-volumelimit.md) | TBD. |
| [KSEVENT_STREAMALLOCATOR enumeration](..\ks\ne-ks-ksevent-streamallocator.md) | TBD. |
| [KSDEVICE_THERMAL_STATE enumeration](..\ks\ne-ks-ksdevice-thermal-state.md) | A KS-defined enumeration for thermal state changes. |
| [KSPIN_MDL_CACHING_EVENT enumeration](..\ks\ne-ks-kspin-mdl-caching-event.md) | This enumeration is used internally by the operating system. |
| [KSRESET enumeration](..\ks\ne-ks-ksreset.md) | TBD. |
| [KSPROPERTY_STREAM enumeration](..\ks\ne-ks-ksproperty-stream.md) | TBD. |
| [KSIRP_REMOVAL_OPERATION enumeration](..\ks\ne-ks-ksirp-removal-operation.md) | TBD. |
| [KSINTERFACE_STANDARD enumeration](..\ks\ne-ks-ksinterface-standard.md) | TBD. |
| [KSMETHOD_STREAMIO enumeration](..\ks\ne-ks-ksmethod-streamio.md) | TBD. |
| [KSOBJECTTYPE enumeration](..\ks\ne-ks-ksobjecttype.md) | The KSOBJECTTYPE enumeration lists different types of kernel streaming objects. |
| [KSSTREAM_POINTER_STATE enumeration](..\ks\ne-ks-ksstream-pointer-state.md) | TBD. |
| [KSEVENTS_LOCKTYPE enumeration](..\ks\ne-ks-ksevents-locktype.md) | The KSEVENTS_LOCKTYPE enumeration identifies the type of exclusion lock. The types are used with EventFlags in several event-set helper functions. |
| [KSEVENT_CLOCK_POSITION enumeration](..\ks\ne-ks-ksevent-clock-position.md) | TBD. |
| [PKSSTATE enumeration](..\ks\ne-ks-pksstate.md) | The KSSTATE enumeration lists possible states of a kernel streaming object. |
| [PKSPIN_COMMUNICATION enumeration](..\ks\ne-ks-pkspin-communication.md) | TBD. |
| [KSEVENT_CONNECTION enumeration](..\ks\ne-ks-ksevent-connection.md) | TBD. |
| [KS_SEEKING_CAPABILITIES enumeration](..\ks\ne-ks-ks-seeking-capabilities.md) | TBD. |
| [KSPROPERTY_CLOCK enumeration](..\ks\ne-ks-ksproperty-clock.md) | TBD. |
| [KSPPROPERTY_ALLOCATOR_MDLCACHING enumeration](..\ks\ne-ks-kspproperty-allocator-mdlcaching.md) | This enumeration is used internally by the operating system. |
| [KSPROPERTY_STREAMINTERFACE enumeration](..\ks\ne-ks-ksproperty-streaminterface.md) | TBD. |
| [KSPROPERTY_GM enumeration](..\ks\ne-ks-ksproperty-gm.md) | TBD. |
| [KSINTERFACE_FILEIO enumeration](..\ks\ne-ks-ksinterface-fileio.md) | TBD. |
| [KSPROPERTY_TOPOLOGY enumeration](..\ks\ne-ks-ksproperty-topology.md) | TBD. |
| [KSCOMPLETION_INVOCATION enumeration](..\ks\ne-ks-kscompletion-invocation.md) | TBD. |
| [KSTARGET_STATE enumeration](..\ks\ne-ks-kstarget-state.md) | TBD. |
| [KS_SEEKING_FLAGS enumeration](..\ks\ne-ks-ks-seeking-flags.md) | The KS_SEEKING_FLAGS enumeration lists positioning options that can be used in conjunction with the KSPROPERTY_POSITIONS structure. |
| [KSPROPERTY_MEDIASEEKING enumeration](..\ks\ne-ks-ksproperty-mediaseeking.md) | TBD. |
| [KSPROPERTY_CONNECTION enumeration](..\ks\ne-ks-ksproperty-connection.md) | TBD. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [KsPinGetFirstCloneStreamPointer function](..\ks\nf-ks-kspingetfirstclonestreampointer.md) | The KsPinGetFirstCloneStreamPointer function returns the first cloned stream pointer on Pin. |
| [KsAddObjectCreateItemToDeviceHeader function](..\ks\nf-ks-ksaddobjectcreateitemtodeviceheader.md) | The KsAddObjectCreateItemToDeviceHeader function adds the specified create-item to an empty item in the previously allocated create item list for this device header. |
| [KsGateRemoveOffInputFromOr function](..\ks\nf-ks-ksgateremoveoffinputfromor.md) | The KsGateRemoveOffInputFromOr function removes an existing input that is in the OFF state from an OR gate. |
| [KsReleaseDeviceSecurityLock function](..\ks\nf-ks-ksreleasedevicesecuritylock.md) | The KsReleaseDeviceSecurityLock function releases a previously acquired security lock on the device object header. |
| [KsDeviceRegisterAggregatedClientUnknown function](..\ks\nf-ks-ksdeviceregisteraggregatedclientunknown.md) | This inline function is a wrapper for KsRegisterAggregatedClientUnknown. |
| [KsGateCaptureThreshold function](..\ks\nf-ks-ksgatecapturethreshold.md) | The KsGateCaptureThreshold function is used to capture an ON input of an AND gate specified by Gate. |
| [KsDeviceRegisterAdapterObject function](..\ks\nf-ks-ksdeviceregisteradapterobject.md) | The KsDeviceRegisterAdapterObject function registers a DMA adapter object with AVStream for performing scatter/gather DMA on the specified device. All drivers compiled for Win64 should use IKsDeviceFunctions |
| [KsGetNextSibling function](..\ks\nf-ks-ksgetnextsibling.md) | The KsGetNextSibling function returns the next sibling of a given object. |
| [KsPinAcquireProcessingMutex function](..\ks\nf-ks-kspinacquireprocessingmutex.md) | The KsPinAcquireProcessingMutex function acquires the processing mutex for the AVStream pin specified by Pin. |
| [KsFilterFactoryGetNextSiblingFilterFactory function](..\ks\nf-ks-ksfilterfactorygetnextsiblingfilterfactory.md) | The KsFilterFactoryGetNextSiblingFilterFactory function returns the next filter factory belonging to the parent device of FilterFactory. |
| [KsPinGetAndGate function](..\ks\nf-ks-kspingetandgate.md) | The KsPinGetAndGate function returns the processing control gate for Pin. |
| [KsGateTerminateOr function](..\ks\nf-ks-ksgateterminateor.md) | The KsGateTerminateOr function deletes an existing OR gate and removes an input from any attached AND gate. |
| [KsPinSubmitFrameMdl function](..\ks\nf-ks-kspinsubmitframemdl.md) | If a pin has been placed into injection mode by a call to KsPinRegisterFrameReturnCallback, the KsPinSubmitFrameMdl function submits a frame directly into the transport circuit. |
| [KsStreamPointerCancelTimeout function](..\ks\nf-ks-ksstreampointercanceltimeout.md) | The KsStreamPointerCancelTimeout function cancels a previously scheduled time-out callback on the specified stream pointer. |
| [KsAddDevice function](..\ks\nf-ks-ksadddevice.md) | The KsAddDevice function is the default AddDevice handler installed by KsInitializeDriver. |
| [KsAcquireDevice function](..\ks\nf-ks-ksacquiredevice.md) | The KsAcquireDevice function gains synchronous access for Device by acquiring the device mutex. |
| [KsFreeEventList function](..\ks\nf-ks-ksfreeeventlist.md) | The KsFreeEventList function handles freeing all events from a specified list, with the assumption that these events are composed of KSEVENT_ENTRY structures. This function can only be called at PASSIVE_LEVEL. |
| [KsFilterGetAndGate function](..\ks\nf-ks-ksfiltergetandgate.md) | The KsFilterGetAndGate function returns Filter's AND gate. |
| [KsGenerateDataEvent function](..\ks\nf-ks-ksgeneratedataevent.md) | The KsGenerateDataEvent function generates one of the standard event notifications when given an event entry structure and callback data. |
| [KsGateTurnInputOn function](..\ks\nf-ks-ksgateturninputon.md) | The KsGateTurnInputOn function turns on an existing input to Gate. |
| [KsPinPropertyHandler function](..\ks\nf-ks-kspinpropertyhandler.md) | The KsPinPropertyHandler function performs standard handling of the static members of the KSPROPSETID_Pin property set. This handling does not include KSPROPERTY_PIN_CINSTANCES or KSPROPERTY_PIN_DATAINTERSECTION. |
| [KsGateInitialize function](..\ks\nf-ks-ksgateinitialize.md) | The KsGateInitialize function initializes a gate for use. |
| [KsAllocateDeviceHeader function](..\ks\nf-ks-ksallocatedeviceheader.md) | The KsAllocateDeviceHeader function allocates and initializes the required device extension header. |
| [KsMergeAutomationTables function](..\ks\nf-ks-ksmergeautomationtables.md) | The KsMergeAutomationTables function merges two automation tables. |
| [KsSetInformationFile function](..\ks\nf-ks-kssetinformationfile.md) | The KsSetInformationFile function performs an information set against the specified file object. The function attempts to use FastIoDispatch if possible, or it generates an information set against the device object. |
| [KsPinGetReferenceClockInterface function](..\ks\nf-ks-kspingetreferenceclockinterface.md) | The KsPinGetReferenceClockInterface function returns a COM style interface to the reference clock associated with Pin. This interface pointer will be an IKsReferenceClock interface. |
| [KsAllocateObjectBag function](..\ks\nf-ks-ksallocateobjectbag.md) | The KsAllocateObjectBag function creates an object bag and associates it with a KSDEVICE. |
| [KsCreateAllocator function](..\ks\nf-ks-kscreateallocator.md) | The KsCreateAllocator function creates a handle to an allocator for the given sink connection handle. This function does not complete the IRP or set the status in the IRP. |
| [KsStreamPointerClone function](..\ks\nf-ks-ksstreampointerclone.md) | The KsStreamPointerClone function creates a clone of a given stream pointer. |
| [KsPinDataIntersectionEx function](..\ks\nf-ks-kspindataintersectionex.md) | The KsPinDataIntersectionEx function handles the KSPROPERTY_PIN_DATAINTERSECTION through a callback function. |
| [KsStreamIo function](..\ks\nf-ks-ksstreamio.md) | The KsStreamIo function performs a stream read or write against the specified file object. The function attempts to use FastIoDispatch if possible, or it generates a read or write request against the device object. |
| [KsIncrementCountedWorker function](..\ks\nf-ks-ksincrementcountedworker.md) | Increments the current worker count, and optionally queues the counted work item with the worker previously created by KsRegisterCountedWorker. |
| [KsProcessPinUpdate function](..\ks\nf-ks-ksprocesspinupdate.md) | The KsProcessPinUpdate function is called from within a filter-centric filter's AVStrMiniFilterProcess dispatch to update a process pin. |
| [KsCreatePin function](..\ks\nf-ks-kscreatepin~r1.md) | The KsCreatePin function passes a connection request to a device, creating a pin instance. This function can only be called at PASSIVE_LEVEL for kernel-mode clients. |
| [KsDeviceGetFirstChildFilterFactory function](..\ks\nf-ks-ksdevicegetfirstchildfilterfactory.md) | The KsDeviceGetFirstChildFilterFactory function returns the first child filter factory belonging to a given AVStream device. |
| [KsCreatePin function](..\ks\nf-ks-kscreatepin.md) | The KsCreatePin function passes a connection request to a device, creating a pin instance. This function can only be called at PASSIVE_LEVEL for kernel-mode clients. |
| [KsPinAttemptProcessing function](..\ks\nf-ks-kspinattemptprocessing.md) | The KsPinAttemptProcessing function is used to resume processing on a specific pin on a pin-centric filter. It attempts to initiate processing on Pin by sending a processing dispatch call to Pin's processing object. |
| [KsPinGetAvailableByteCount function](..\ks\nf-ks-kspingetavailablebytecount.md) | The KsPinGetAvailableByteCount routine outputs the number of bytes of input data ahead of the leading edge and the number of bytes of output buffer ahead of the leading edge, both for the queue of a caller-specified pin. |
| [KsValidateConnectRequest function](..\ks\nf-ks-ksvalidateconnectrequest.md) | The KsValidateConnectRequest function validates a connection request and returns a pointer to the connection structure associated with the request.This function can only be called at PASSIVE_LEVEL. |
| [KsFilterFactoryRegisterAggregatedClientUnknown function](..\ks\nf-ks-ksfilterfactoryregisteraggregatedclientunknown.md) | This inline function is a wrapper for KsRegisterAggregatedClientUnknown. |
| [KsEnableEvent function](..\ks\nf-ks-ksenableevent.md) | The KsEnableEvent function enables events requested through IOCTL_KS_ENABLE_EVENT. It responds to all event identifiers defined by the sets. This function can only be called at PASSIVE_LEVEL. |
| [KsAcquireResetValue function](..\ks\nf-ks-ksacquireresetvalue.md) | The KsAcquireResetValue function retrieves the current reset state from an IOCTL_KS_RESET_STATE IRP. |
| [IKsControl::KsEvent method](..\ks\nf-ks-ikscontrol-ksevent.md) | The IKsControl |
| [KsGetPinFromFileObject function](..\ks\nf-ks-ksgetpinfromfileobject.md) | The KsGetPinFromFileObject function returns the AVStream pin object associated with FileObject. |
| [KsPropertyHandler function](..\ks\nf-ks-kspropertyhandler.md) | Drivers call KsPropertyHandler function for IRP handling. |
| [KsQueryObjectCreateItem function](..\ks\nf-ks-ksqueryobjectcreateitem.md) | The KsQueryObjectCreateItem function returns the create item assigned to the object when created. |
| [KsPinRegisterPowerCallbacks function](..\ks\nf-ks-kspinregisterpowercallbacks.md) | The KsPinRegisterPowerCallbacks function registers power management callbacks for Pin. |
| [KsFilterAddTopologyConnections function](..\ks\nf-ks-ksfilteraddtopologyconnections.md) | The KsFilterAddTopologyConnections function adds new topology connections to a filter. |
| [KsMethodHandlerWithAllocator function](..\ks\nf-ks-ksmethodhandlerwithallocator.md) | The KsMethodHandlerWithAllocator functions performs the same handling as KsMethodHandler, with the same restrictions, but allows an optional allocator callback to be used to provide a buffer for the parameters. |
| [KsGateInitializeAnd function](..\ks\nf-ks-ksgateinitializeand.md) | The KsGateInitializeAnd function initializes a KSGATE structure as an AND gate and attaches it to the OR gate specified by NextOrGate. |
| [KsFilterAttemptProcessing function](..\ks\nf-ks-ksfilterattemptprocessing.md) | The KsFilterAttemptProcessing function attempts to initiate processing on Filter. |
| [KsCopyObjectBagItems function](..\ks\nf-ks-kscopyobjectbagitems.md) | The KsCopyObjectBagItems function copies all items from one object bag into another. |
| [KsFilterGetDevice function](..\ks\nf-ks-ksfiltergetdevice.md) | The KsFilterGetDevice function returns the AVStream device to which Filter belongs. |
| [KsAddItemToObjectBag function](..\ks\nf-ks-ksadditemtoobjectbag.md) | The KsAddItemToObjectBag function adds an object or block of memory to the given object bag. |
| [KsFilterFactorySetDeviceClassesState function](..\ks\nf-ks-ksfilterfactorysetdeviceclassesstate.md) | The KsFilterFactorySetDeviceClassesState function enables or disables the device classes that have been registered by a given filter factory. |
| [KsSetTargetDeviceObject function](..\ks\nf-ks-kssettargetdeviceobject.md) | The KsSetTargetDeviceObject function sets the target device object of an object. The function adds the object header to a list of object headers that have target devices. |
| [KsGetDefaultClockTime function](..\ks\nf-ks-ksgetdefaultclocktime.md) | The KsGetDefaultClockTime function gets the current time of the clock.The function can be called at DISPATCH_LEVEL. |
| [KsAcquireDeviceSecurityLock function](..\ks\nf-ks-ksacquiredevicesecuritylock.md) | The KsAcquireDeviceSecurityLock function acquires the security lock associated with a device object. |
| [KsFilterCreateNode function](..\ks\nf-ks-ksfiltercreatenode.md) | The KsFilterCreateNode function creates a new topology node on the specified filter. |
| [KsPinGetOuterUnknown function](..\ks\nf-ks-kspingetouterunknown.md) | The KsPinGetOuterUnknown function returns the outer IUnknown of the pin specified by Pin. |
| [KsAllocateDefaultClock function](..\ks\nf-ks-ksallocatedefaultclock.md) | The KsAllocateDefaultClock function allocates and initializes the default clock structure. |
| [KsEdit function](..\ks\nf-ks-ksedit.md) | The _KsEdit function guarantees that a given item is dynamically allocated and associated with an AVStream object through the object bag. |
| [KsValidateClockCreateRequest function](..\ks\nf-ks-ksvalidateclockcreaterequest.md) | The KsValidateClockCreateRequest function validates the clock creation request and returns the create structure associated with the request.This can only be called at PASSIVE_LEVEL. |
| [KsGenerateEventList function](..\ks\nf-ks-ksgenerateeventlist.md) | The KsGenerateEventList function enumerates the event list and searches for the specified event to generate. |
| [KsCancelIo function](..\ks\nf-ks-kscancelio.md) | The KsCancelIo function cancels all IRPs on the specified cancel list. If an IRP on the list does not have a cancel routine, only the cancel bit is set in the IRP. The function can be called at IRQ level DISPATCH_LEVEL or lower. |
| [KsFilterGetFirstChildPin function](..\ks\nf-ks-ksfiltergetfirstchildpin.md) | The KsFilterGetFirstChildPin function returns the first instantiated pin of type PinID on the filter specified by Filter. |
| [KsStreamPointerGetIrp function](..\ks\nf-ks-ksstreampointergetirp.md) | The KsStreamPointerGetIrp function returns the IRP associated with the frame that is referenced by the given stream pointer. |
| [KsReferenceBusObject function](..\ks\nf-ks-ksreferencebusobject.md) | References the bus Physical device object. |
| [KsAllocateExtraData function](..\ks\nf-ks-ksallocateextradata.md) | The KsAllocateExtraData function is used with streaming IRPs to allocate a buffer to contain additional header data. A pointer to the allocated buffer is returned, and the buffer must eventually be freed by the caller. |
| [KsFilterReleaseControl function](..\ks\nf-ks-ksfilterreleasecontrol.md) | The KsFilterReleaseControl function releases the control mutex for the AVStream filter specified by Filter. |
| [KsValidateTopologyNodeCreateRequest function](..\ks\nf-ks-ksvalidatetopologynodecreaterequest.md) | The KsValidateTopologyNodeCreateRequest function validates a topology node creation request and returns the create structure associated with the request. The function can only be called at PASSIVE_LEVEL. |
| [KsFilterGetParentFilterFactory function](..\ks\nf-ks-ksfiltergetparentfilterfactory.md) | The KsFilterGetParentFilterFactory function returns the parent filter factory of the given filter. |
| [KsLoadResource function](..\ks\nf-ks-ksloadresource.md) | Copies (loads) a resource from the given image. |
| [KsSetDefaultClockState function](..\ks\nf-ks-kssetdefaultclockstate.md) | The KsSetDefaultClockState function sets the current state of the clock that is used to reflect the current state of the underlying filter pin. |
| [KsDeviceGetOuterUnknown function](..\ks\nf-ks-ksdevicegetouterunknown.md) | The KsDeviceGetOuterUnknown function returns the outer IUnknown of the AVStream device specified by Device. |
| [KsDereferenceBusObject function](..\ks\nf-ks-ksdereferencebusobject.md) | Dereferences the bus Physical Device Object. |
| [KsGenerateEvents function](..\ks\nf-ks-ksgenerateevents.md) | The KsGenerateEvents function generates events of an indicated type that are present in Object's event list. |
| [KsStreamPointerGetMdl function](..\ks\nf-ks-ksstreampointergetmdl.md) | The KsStreamPointerGetMdl function returns the MDL associated with the frame referenced by StreamPointer. |
| [KsReadFile function](..\ks\nf-ks-ksreadfile.md) | The KsReadFile function performs a read against the specified file object. |
| [IKsReferenceClock::GetCorrelatedPhysicalTime method](..\ks\nf-ks-iksreferenceclock-getcorrelatedphysicaltime.md) | The IKsReferenceClock |
| [KsSetDefaultClockTime function](..\ks\nf-ks-kssetdefaultclocktime.md) | The KsSetDefaultClockTime function sets the current time of the clock. |
| [KsStreamPointerAdvanceOffsetsAndUnlock function](..\ks\nf-ks-ksstreampointeradvanceoffsetsandunlock.md) | The KsStreamPointerAdvanceOffsetsAndUnlock function advances StreamPointer the specified number of bytes into the stream (adjusting the OffsetIn and OffsetOut fields of StreamPointer as requested) and unlocks it. |
| [KsCreateDefaultSecurity function](..\ks\nf-ks-kscreatedefaultsecurity.md) | The KsCreateDefaultSecurity function creates a security descriptor with default security, optionally inheriting parameters from a parent security descriptor. |
| [KsPinGetCopyRelationships function](..\ks\nf-ks-kspingetcopyrelationships.md) | The KsPinGetCopyRelationships function returns copy relationship information for a pin that is contained within a pin-centric filter. |
| [KsAllocateObjectHeader function](..\ks\nf-ks-ksallocateobjectheader.md) | The KsAllocateObjectHeader function initializes the required file context header. |
| [KsGetDefaultClockState function](..\ks\nf-ks-ksgetdefaultclockstate.md) | The KsGetDefaultClockState function gets the current state of the clock.The function can be called at DISPATCH_LEVEL. |
| [KsPinDataIntersection function](..\ks\nf-ks-kspindataintersection.md) | The KsPinDataIntersection function handles the KSPROPERTY_PIN_DATAINTERSECTION property through a callback function and performs much of the initial validation of the parameters that are passed. |
| [KsCacheMedium function](..\ks\nf-ks-kscachemedium.md) | The KsCacheMedium function improves graph building performance of pins that use Mediums to define connectivity. |
| [KsPinAcquireControl function](..\ks\nf-ks-kspinacquirecontrol.md) | The KsPinAcquireControl function acquires the control mutex for the AVStream pin specified by Pin. |
| [KsStreamPointerAdvance function](..\ks\nf-ks-ksstreampointeradvance.md) | The KsStreamPointerAdvance function advances a stream pointer to the next data frame. |
| [KsFilterAcquireControl function](..\ks\nf-ks-ksfilteracquirecontrol.md) | The KsFilterAcquireControl function acquires the filter control mutex for the AVStream filter specified by Filter. |
| [KsDeviceSetBusData function](..\ks\nf-ks-ksdevicesetbusdata.md) | The KsDeviceSetBusData function writes data to the bus on which the specified AVStream device resides. |
| [KsDispatchFastIoDeviceControlFailure function](..\ks\nf-ks-ksdispatchfastiodevicecontrolfailure.md) | The KsDispatchFastIoDeviceControlFailure function is used in a KSDISPATCH_TABLE.FastDeviceIoControl entry that are not handled. The function should always return FALSE. |
| [KsGetObjectTypeFromFileObject function](..\ks\nf-ks-ksgetobjecttypefromfileobject.md) | The KsGetObjectTypeFromFileObject function returns the AVStream object type that is associated with a given file object. |
| [KsPinGetConnectedPinFileObject function](..\ks\nf-ks-kspingetconnectedpinfileobject.md) | The KsPinGetConnectedPinFileObject function returns the file object for the pin to which Pin is connected. Works only for source pins. |
| [KsGetObjectFromFileObject function](..\ks\nf-ks-ksgetobjectfromfileobject.md) | The KsGetObjectFromFileObject function returns the AVStream object cast to PVOID from FileObject. |
| [KsCreateFilterFactory function](..\ks\nf-ks-kscreatefilterfactory.md) | The KsCreateFilterFactory function adds a filter factory to a given device. |
| [KsGateAddOnInputToOr function](..\ks\nf-ks-ksgateaddoninputtoor.md) | The KsGateAddOnInputToOr function adds a new input in the ON state to a given OR gate. |
| [KsReleaseControl function](..\ks\nf-ks-ksreleasecontrol.md) | The KsReleaseControl function releases the control mutex for Object. |
| [KsDispatchInvalidDeviceRequest function](..\ks\nf-ks-ksdispatchinvaliddevicerequest.md) | The KsDispatchInvalidDeviceRequest function is used in KSDISPATCH_TABLE entries that are not handled and that need to return STATUS_INVALID_DEVICE_REQUEST. |
| [KsFilterRegisterAggregatedClientUnknown function](..\ks\nf-ks-ksfilterregisteraggregatedclientunknown.md) | This inline function is a wrapper for KsRegisterAggregatedClientUnknown. |
| [KsGetObjectTypeFromIrp function](..\ks\nf-ks-ksgetobjecttypefromirp.md) | The KsGetObjectTypeFromIrp function returns the AVStream object type that is associated with a given IRP. |
| [KsStreamPointerUnlock function](..\ks\nf-ks-ksstreampointerunlock.md) | The KsStreamPointerUnlock function unlocks a stream pointer that has previously been locked by an acquisition function (KsGetXxxEdgeStreamPointer) or by KsStreamPointerLock. |
| [KsInitializeDevice function](..\ks\nf-ks-ksinitializedevice.md) | The KsInitializeDevice function is called by AVStream to initialize the AVStream device class from within KsCreateDevice. |
| [KsStreamPointerLock function](..\ks\nf-ks-ksstreampointerlock.md) | The KsStreamPointerLock function attempts to lock the specified stream pointer. |
| [KsDefaultAddEventHandler function](..\ks\nf-ks-ksdefaultaddeventhandler.md) | The KsDefaultAddEventHandler function is a default routine to handle event 'add' requests. |
| [KsFreeObjectCreateItem function](..\ks\nf-ks-ksfreeobjectcreateitem.md) | Frees the slot for the specified create item. |
| [KsNullDriverUnload function](..\ks\nf-ks-ksnulldriverunload.md) | The KsNullDriverUnload function is a default function a driver can use when it has no other tasks to do in its unload function, but must still allow the device to be unloaded by its presence. |
| [KsCreateClock2 function](..\ks\nf-ks-kscreateclock2.md) | Creates a handle to a clock instance. Call this function after the Component Object Model (COM) is initialized. |
| [KsPinSubmitFrame function](..\ks\nf-ks-kspinsubmitframe.md) | If a pin has been placed into injection mode by a call to KsPinRegisterFrameReturnCallback, the KsPinSubmitFrame function submits a frame directly into the transport circuit. |
| [KsHandleSizedListQuery function](..\ks\nf-ks-kshandlesizedlistquery.md) | The KsHandleSizedListQuery function, depending on the length of the system buffer, returns either the size of the buffer needed, number of entries in the specified data list, or copies the entries themselves. |
| [KsCreateAllocator function](..\ks\nf-ks-kscreateallocator~r1.md) | The KsCreateAllocator function creates a handle to an allocator for the given sink connection handle. This function does not complete the IRP or set the status in the IRP. |
| [IKsReferenceClock::GetCorrelatedTime method](..\ks\nf-ks-iksreferenceclock-getcorrelatedtime.md) | The IKsReferenceClock |
| [IKsControl::KsProperty method](..\ks\nf-ks-ikscontrol-ksproperty.md) | The IKsControl |
| [KsGateAddOnInputToAnd function](..\ks\nf-ks-ksgateaddoninputtoand.md) | The KsGateAddOnInputToAnd function adds a new input in the ON state to a given AND gate. |
| [KsGetDeviceForDeviceObject function](..\ks\nf-ks-ksgetdevicefordeviceobject.md) | The KsGetDeviceForDeviceObject function returns the AVStream device structure for a given functional device object. |
| [KsGateTurnInputOff function](..\ks\nf-ks-ksgateturninputoff.md) | The KsGateTurnInputOff function turns off an existing input to Gate. |
| [KsFilterAcquireProcessingMutex function](..\ks\nf-ks-ksfilteracquireprocessingmutex.md) | The KsFilterAcquireProcessingMutex function acquires the processing mutex for a specified AVStream filter. |
| [KsFilterFactoryGetSymbolicLink function](..\ks\nf-ks-ksfilterfactorygetsymboliclink.md) | The KsFilterFactoryGetSymbolicLink function returns the symbolic link associated with a given filter factory. |
| [KsForwardIrp function](..\ks\nf-ks-ksforwardirp.md) | The KsForwardIrp function forwards an IRP to the specified driver after initializing the next stack location and setting the file object. |
| [KsQueueWorkItem function](..\ks\nf-ks-ksqueueworkitem.md) | The KsQueueWorkItem function queues the specified work item with a worker previous created by the KsRegisterWorker function. |
| [KsDispatchIrp function](..\ks\nf-ks-ksdispatchirp.md) | KsDispatchIrp calls a dispatch routine corresponding to the function code of the specified IRP. KsDispatchIrp then returns the status code from this call. |
| [IKsReferenceClock::GetPhysicalTime method](..\ks\nf-ks-iksreferenceclock-getphysicaltime.md) | The IKsReferenceClock |
| [KsCreateTopologyNode function](..\ks\nf-ks-kscreatetopologynode.md) | The KsCreateTopologyNode function creates a handle to a topology node instance. The function can only be called at PASSIVE_LEVEL. |
| [KsDeviceGetBusData function](..\ks\nf-ks-ksdevicegetbusdata.md) | The KsDeviceGetBusData function reads data from the bus where the given AVStream device resides. |
| [KsFilterAddEvent function](..\ks\nf-ks-ksfilteraddevent.md) | The KsFilterAddEvent function adds an event to Filter's event list. |
| [KsGateRemoveOffInputFromAnd function](..\ks\nf-ks-ksgateremoveoffinputfromand.md) | The KsGateRemoveOffInputFromAnd function removes an existing input that is in the OFF state from an AND gate. |
| [KsGateGetStateUnsafe function](..\ks\nf-ks-ksgategetstateunsafe.md) | The KsGateGetStateUnsafe function returns the state of the given gate (open or closed) in an unsafe manner, that is without regard to synchronization. |
| [KsCreateDefaultClock function](..\ks\nf-ks-kscreatedefaultclock.md) | Given an IRP_MJ_CREATE request, the KsCreateDefaultClock function creates a default clock that uses the system clock as a time base and associates the IoGetCurrentIrpStackLocation(Irp)-&gt;FileObject with the clock using an internal dispatch table (KSDISPATCH_TABLE). Does not complete the IRP or set the status in the IRP.The KsCreateDefaultClock function can only be called at PASSIVE_LEVEL. |
| [KsMoveIrpsOnCancelableQueue function](..\ks\nf-ks-ksmoveirpsoncancelablequeue.md) | The KsMoveIrpsOnCancelableQueue function moves the specified IRPs from the SourceList parameter to the DestinationList parameter depending on the value returned from the minidriver-defined KStrIrpListCallback function. |
| [KsGetFilterFromFileObject function](..\ks\nf-ks-ksgetfilterfromfileobject.md) | The KsGetFilterFromFileObject function returns the AVStream filter object associated with FileObject. |
| [KsPinRegisterFrameReturnCallback function](..\ks\nf-ks-kspinregisterframereturncallback.md) | The KsPinRegisterFrameReturnCallback function registers a frame return callback with AVStream for a given pin. |
| [KsGateTerminateAnd function](..\ks\nf-ks-ksgateterminateand.md) | The KsGateTerminateAnd function deletes an existing AND gate and removes an input from any attached OR gate. |
| [KsDefaultDeviceIoCompletion function](..\ks\nf-ks-ksdefaultdeviceiocompletion.md) | The KsDefaultDeviceIoCompletion function is used to return a default response and to complete any device I/O control. |
| [KsReleaseDevice function](..\ks\nf-ks-ksreleasedevice.md) | The KsReleaseDevice function releases the device mutex and exits the critical region. |
| [KsQueryObjectAccessMask function](..\ks\nf-ks-ksqueryobjectaccessmask.md) | The KsQueryObjectAccessMask function returns the access originally granted to the first client that created a handle on the associated object. Access cannot be changed by duplicating handles. |
| [KsGetParent function](..\ks\nf-ks-ksgetparent.md) | The KsGetParent function acquires the parent of the given object. |
| [KsFilterFactoryAddCreateItem function](..\ks\nf-ks-ksfilterfactoryaddcreateitem.md) | The KsFilterFactoryAddCreateItem function adds a new create item for the specified filter factory. |
| [KsStreamPointerGetNextClone function](..\ks\nf-ks-ksstreampointergetnextclone.md) | The KsStreamPointerGetNextClone function returns the clone stream pointer that was cloned immediately after the specified clone. |
| [KsFastMethodHandler function](..\ks\nf-ks-ksfastmethodhandler.md) | The KsFastMethodHandler function handles fast methods requested through IOCTL_KS_METHOD. It responds to all method identifiers defined by the sets that are also contained in the fast I/O list. This function can only be called at PASSIVE_LEVEL. |
| [KsFreeObjectBag function](..\ks\nf-ks-ksfreeobjectbag.md) | The KsFreeObjectBag function empties and frees an object bag. |
| [IKsReferenceClock::GetState method](..\ks\nf-ks-iksreferenceclock-getstate.md) | The IKsReferenceClock |
| [KsCreateDevice function](..\ks\nf-ks-kscreatedevice.md) | The KsCreateDevice function creates an AVStream device. |
| [KsUnserializeObjectPropertiesFromRegistry function](..\ks\nf-ks-ksunserializeobjectpropertiesfromregistry.md) | The KsUnserializeObjectPropertiesFromRegistry function, when given a destination object and a registry path, enumerates the named values and applies them as serialized data to the specified property sets listed in the serialized data. |
| [KsAllocateObjectCreateItem function](..\ks\nf-ks-ksallocateobjectcreateitem.md) | The KsAllocateObjectCreateItem function allocates a slot for the specified create item, optionally allocating space for and copying the create item data as well. |
| [KsFastPropertyHandler function](..\ks\nf-ks-ksfastpropertyhandler.md) | The KsFastPropertyHandler function handles fast property requests through IOCTL_KS_PROPERTY. It responds to all property identifiers defined by the sets that are also contained in the fast I/O list. This function can only be called at PASSIVE_LEVEL. |
| [IKsDeviceFunctions::RegisterAdapterObjectEx method](..\ks\nf-ks-iksdevicefunctions-registeradapterobjectex.md) | The IKsDeviceFunctions |
| [KsPinGetConnectedPinInterface function](..\ks\nf-ks-kspingetconnectedpininterface.md) | The KsPinGetConnectedPinInterface function queries the pin to which Pin is connected for a COM style interface. |
| [KsDispatchSetSecurity function](..\ks\nf-ks-ksdispatchsetsecurity.md) | The KsDispatchSetSecurity function is used in the KSDISPATCH_TABLE.SetSecurity entry to handle setting the current security descriptor. |
| [KsAddEvent function](..\ks\nf-ks-ksaddevent.md) | The KsAddEvent function adds an event to Object's event list. |
| [KsMapModuleName function](..\ks\nf-ks-ksmapmodulename.md) | The KsMapModuleName function returns the image name and resource identifier that corresponds to the PhysicalDeviceObject and ModuleName parameters. |
| [KsFreeObjectCreateItemsByContext function](..\ks\nf-ks-ksfreeobjectcreateitemsbycontext.md) | Frees all create items with a specific context. |
| [KsFilterCreatePinFactory function](..\ks\nf-ks-ksfiltercreatepinfactory.md) | The KsFilterCreatePinFactory function creates a new pin factory on the specified filter. |
| [KsGenerateThermalEvent function](..\ks\nf-ks-ksgeneratethermalevent.md) | This function is used by clients (miniport drivers) that do not want to subscribe to the thermal manager, but want to do their own thermal management. |
| [KsCompletePendingRequest function](..\ks\nf-ks-kscompletependingrequest.md) | The KsCompletePendingRequest function is used to complete an I/O request in response to which an AVStream dispatch function previously returned STATUS_PENDING. |
| [KsSynchronousIoControlDevice function](..\ks\nf-ks-kssynchronousiocontroldevice.md) | The KsSynchronousIoControlDevice function performs a synchronous device I/O control on the target device object. It waits in a nonalertable state until the I/O completes. This function can only be called at PASSIVE_LEVEL. |
| [KsDeviceRegisterThermalDispatch function](..\ks\nf-ks-ksdeviceregisterthermaldispatch.md) | This function is used by the Avstream miniport driver to register callbacks for thermal notifications with the KS port driver. |
| [KsFilterFactoryUpdateCacheData function](..\ks\nf-ks-ksfilterfactoryupdatecachedata.md) | The KsFilterFactoryUpdateCacheData function updates the FilterData registry key and the Medium cache (a set of registry keys) for a given filter factory. |
| [KsPinHandshake function](..\ks\nf-ks-kspinhandshake.md) | The KsPinHandshake function attempts a protocol handshake with a connected pin. |
| [KsGetOuterUnknown function](..\ks\nf-ks-ksgetouterunknown.md) | The KsGetOuterUnknown function returns the outer IUnknown of a given AVStream object. |
| [KsTopologyPropertyHandler function](..\ks\nf-ks-kstopologypropertyhandler.md) | The KsTopologyPropertyHandler function performs standard handling of the static members of the KSPROPSETID_Topology Property Set. The function uses the KSTOPOLOGY structure, which describes the set of information that is returned by this property set. |
| [KsGateAddOffInputToAnd function](..\ks\nf-ks-ksgateaddoffinputtoand.md) | The KsGateAddOffInputToAnd function adds a new input in the OFF state to a given AND gate. |
| [KsCreateAllocator2 function](..\ks\nf-ks-kscreateallocator2.md) | Creates a handle to an allocator for the given sink connection handle. This function does not complete the IRP or set the status in the IRP. |
| [KsAllocateDefaultClockEx function](..\ks\nf-ks-ksallocatedefaultclockex.md) | The KsAllocateDefaultClockEx function allocates and initializes the default clock structure. |
| [KsPinGetNextSiblingPin function](..\ks\nf-ks-kspingetnextsiblingpin.md) | The KsPinGetNextSiblingPin function returns the next instantiated pin of the same type and on the same filter as Pin. |
| [KsInitializeDriver function](..\ks\nf-ks-ksinitializedriver.md) | The KsInitializeDriver function initializes the driver object of an AVStream minidriver. |
| [KsSetTargetState function](..\ks\nf-ks-kssettargetstate.md) | Sets the enabled state of a target device associated with the specified object header. |
| [KsPinGetTrailingEdgeStreamPointer function](..\ks\nf-ks-kspingettrailingedgestreampointer.md) | The KsPinGetTrailingEdgeStreamPointer function acquires the trailing edge stream pointer for the queue associated with the specified pin. |
| [KsAcquireCachedMdl function](..\ks\nf-ks-ksacquirecachedmdl.md) | This function is used to acquire the MDL cached by the KS port driver. The function is used by a kernel mode driver to acquire the MDL for a pipeline-supplied sample generated by an Avstream driver. |
| [KsWriteFile function](..\ks\nf-ks-kswritefile.md) | The KsWriteFile function performs a write against the specified file object. |
| [KsUnregisterWorker function](..\ks\nf-ks-ksunregisterworker.md) | The KsUnregisterWorker function allows clients to unregister a worker. |
| [KsPinAddEvent function](..\ks\nf-ks-kspinaddevent.md) | The KsPinAddEvent function adds a specified event to Pin's event list. |
| [KsCreateDefaultAllocator function](..\ks\nf-ks-kscreatedefaultallocator.md) | Given a validated IRP_MJ_CREATE request, the KsCreateDefaultAllocator function creates a default allocator that uses the specified memory pool and associates the IoGetCurrentIrpStackLocation(Irp)-&gt;FileObject with the allocator using an internal dispatch table (KSDISPATCH_TABLE). |
| [KsFilterGenerateEvents function](..\ks\nf-ks-ksfiltergenerateevents.md) | The KsFilterGenerateEvents function generates events of an indicated type that are present in Filter's event list. |
| [KsCreatePin2 function](..\ks\nf-ks-kscreatepin2.md) | Passes a connection request to a device, creating a pin instance. |
| [KsFreeObjectHeader function](..\ks\nf-ks-ksfreeobjectheader.md) | The KsFreeObjectHeader function cleans up and frees a previously allocated object header. |
| [KsStreamPointerSetStatusCode function](..\ks\nf-ks-ksstreampointersetstatuscode.md) | The KsStreamPointerSetStatusCode function allows specification of a successful or unsuccessful error code with which to complete the given IRP. |
| [KsForwardAndCatchIrp function](..\ks\nf-ks-ksforwardandcatchirp.md) | The KsForwardAndCatchIrp function forwards an IRP to the specified driver after initializing the next stack location, and regains control of the IRP on completion from that driver. |
| [KsQueryDevicePnpObject function](..\ks\nf-ks-ksquerydevicepnpobject.md) | The KsQueryDevicePnpObject function returns the PnP device object that can be stored in the device header. This is the next device object on the PnP stack and is the device object that PnP requests are forwarded to if KsDefaultDispatchPnp is used. |
| [KsCreateTopologyNode2 function](..\ks\nf-ks-kscreatetopologynode2.md) | Creates a handle to a topology node instance. |
| [KsRegisterFilterWithNoKSPins function](..\ks\nf-ks-ksregisterfilterwithnokspins.md) | The KsRegisterFilterWithNoKSPins function registers with DirectShow filters that have no kernel streaming pins and, therefore, do not stream in kernel mode. |
| [KsDispatchSpecificMethod function](..\ks\nf-ks-ksdispatchspecificmethod.md) | The KsDispatchSpecificMethod function dispatches a method to a specific handler. The function assumes that the caller has previously dispatched the IRP to a handler through the KsMethodHandler function. The function can only be called at PASSIVE_LEVEL. |
| [KsRegisterWorker function](..\ks\nf-ks-ksregisterworker.md) | The KsRegisterWorker function handles clients registering for use of a thread. |
| [KsReleaseIrpOnCancelableQueue function](..\ks\nf-ks-ksreleaseirponcancelablequeue.md) | The KsReleaseIrpOnCancelableQueue function releases an acquired IRP that is already on a queue that can be canceled. |
| [KsGetNodeIdFromIrp function](..\ks\nf-ks-ksgetnodeidfromirp.md) | The KsGetNodeIdFromIrp function returns the node ID of the node to which Irp was submitted. |
| [KsStreamPointerScheduleTimeout function](..\ks\nf-ks-ksstreampointerscheduletimeout.md) | The KsStreamPointerScheduleTimeout function registers a timeout callback with AVStream for the given stream pointer. |
| [KsSetPowerDispatch function](..\ks\nf-ks-kssetpowerdispatch.md) | Sets the power dispatch function to be called when the driver object receives an IRP_MJ_POWER IRP. |
| [KsRemoveItemFromObjectBag function](..\ks\nf-ks-ksremoveitemfromobjectbag.md) | The KsRemoveItemFromObjectBag function removes an item from an object bag. |
| [KsRegisterCountedWorker function](..\ks\nf-ks-ksregistercountedworker.md) | Handles clients registering for use of a thread. |
| [KsAcquireControl function](..\ks\nf-ks-ksacquirecontrol.md) | The KsAcquireControl function acquires the filter control mutex for Object. |
| [KsGetDevice function](..\ks\nf-ks-ksgetdevice.md) | The KsGetDevice function returns the AVStream device structure to which Object belongs. |
| [KsFilterGetNextSiblingFilter function](..\ks\nf-ks-ksfiltergetnextsiblingfilter.md) | The KsFilterGetNextSiblingFilter function returns the next instantiated filter belonging to the parent filter factory of Filter. |
| [KsPinReleaseProcessingMutex function](..\ks\nf-ks-kspinreleaseprocessingmutex.md) | The KsPinReleaseProcessingMutex function releases the processing mutex for the AVStream pin specified by Pin. |
| [KsPinGetLeadingEdgeStreamPointer function](..\ks\nf-ks-kspingetleadingedgestreampointer.md) | The KsPinGetLeadingEdgeStreamPointer function acquires the leading edge stream pointer for the queue associated with the given pin. |
| [_KsEdit function](..\ks\nf-ks--ksedit.md) | The _KsEdit function guarantees that a given item is dynamically allocated and associated with an AVStream object through the object bag. |
| [KsPinReleaseControl function](..\ks\nf-ks-kspinreleasecontrol.md) | The KsPinReleaseControl function releases the control mutex for the AVStream pin specified by Pin. |
| [KsPinGetParentFilter function](..\ks\nf-ks-kspingetparentfilter.md) | The KsPinGetParentFilter function returns the parent filter of Pin. |
| [KsGateRemoveOnInputFromOr function](..\ks\nf-ks-ksgateremoveoninputfromor.md) | The KsGateRemoveOnInputFromOr function removes an existing input that is in the ON state from an OR gate. |
| [KsGateInitializeOr function](..\ks\nf-ks-ksgateinitializeor.md) | The KsGateInitializeOr function initializes a KSGATE structure as an OR gate and attaches it to the AND gate specified by NextAndGate. |
| [KsFilterFactoryGetDevice function](..\ks\nf-ks-ksfilterfactorygetdevice.md) | The KsFilterFactoryGetDevice function returns the AVStream device to which FilterFactory belongs. |
| [KsDispatchQuerySecurity function](..\ks\nf-ks-ksdispatchquerysecurity.md) | The KsDispatchQuerySecurity function is used in the KSDISPATCH_TABLE.QuerySecurity entry to handle querying about the current security descriptor. |
| [KsCreateClock function](..\ks\nf-ks-kscreateclock.md) | The KsCreateClock function creates a handle to a clock instance. |
| [KsFilterRegisterPowerCallbacks function](..\ks\nf-ks-ksfilterregisterpowercallbacks.md) | The KsFilterRegisterPowerCallbacks function registers power management callbacks for Filter. |
| [KsDecrementCountedWorker function](..\ks\nf-ks-ksdecrementcountedworker.md) | Decrements the current worker count of a worker previous created by KsRegisterCountedWorker. This should be called after each task within a worker has been completed. |
| [KsFreeDefaultClock function](..\ks\nf-ks-ksfreedefaultclock.md) | The KsFreeDefaultClock function frees a default clock structure previously allocated with KsAllocateDefaultClock, taking into account any currently running timer DPCs. |
| [KsGetImageNameAndResourceId function](..\ks\nf-ks-ksgetimagenameandresourceid.md) | The KsGetImageNameAndResourceId function returns the image name and resource identifier that corresponds to the RegKey handle. |
| [KsStreamPointerDelete function](..\ks\nf-ks-ksstreampointerdelete.md) | The KsStreamPointerDelete function deletes a clone stream pointer, releasing a reference on the frame to which this stream pointer referred. |
| [KsDeleteFilterFactory function](..\ks\nf-ks-ksdeletefilterfactory.md) | KsDeleteFilterFactory deletes a given filter factory. |
| [KsPinAttachOrGate function](..\ks\nf-ks-kspinattachorgate.md) | The KsPinAttachOrGate function connects Pin as an input to a previously initialized OR gate, and connects OrGate as an input to the relevant filter's AND gate. |
| [KsFilterFactoryGetParentDevice function](..\ks\nf-ks-ksfilterfactorygetparentdevice.md) | The KsFilterFactoryGetParentDevice function returns the parent device of the given filter factory. |
| [KsFilterFactoryGetOuterUnknown function](..\ks\nf-ks-ksfilterfactorygetouterunknown.md) | The KsFilterFactoryGetOuterUnknown function returns the outer IUnknown of the specified filter factory. |
| [KsSetDevicePnpAndBaseObject function](..\ks\nf-ks-kssetdevicepnpandbaseobject.md) | The KsSetDevicePnpAndBaseObject function sets the PnP device object in the device header, which is the next device object on the PnP stack and is the device object that PnP requests are forwarded to if KsDefaultDispatchPnp is used. |
| [KsEnableEventWithAllocator function](..\ks\nf-ks-ksenableeventwithallocator.md) | The KsEnableEventWithAllocator function enables events requested through IOCTL_KS_ENABLE_EVENT but also allows an optional allocator callback to be used to provide a buffer for the parameters. |
| [KsFreeDeviceHeader function](..\ks\nf-ks-ksfreedeviceheader.md) | The KsFreeDeviceHeader function cleans up and frees a previously allocated device header. |
| [KsDispatchFastReadFailure function](..\ks\nf-ks-ksdispatchfastreadfailure.md) | The KsDispatchFastReadFailure function is used in a KSDISPATCH_TABLE.FastRead entry when fast I/O read is not handled. The function should always return FALSE. |
| [KsPinGenerateEvents function](..\ks\nf-ks-kspingenerateevents.md) | The KsPinGenerateEvents function generates events of an indicated type that are present in Pin's event list. |
| [KsQueryInformationFile function](..\ks\nf-ks-ksqueryinformationfile.md) | The KsQueryInformationFile function performs an information query against the specified file object. The function attempts to use FastIoDispatch if possible, or it generates an information request against the device object. |
| [KsDispatchSpecificProperty function](..\ks\nf-ks-ksdispatchspecificproperty.md) | The KsDispatchSpecificProperty function dispatches the property to a specific handler. |
| [KsGenerateEvent function](..\ks\nf-ks-ksgenerateevent.md) | The KsGenerateEvent function generates a standard event notification given an event entry structure. |
| [KsTerminateDevice function](..\ks\nf-ks-ksterminatedevice.md) | The KsTerminateDevice function removes an AVStream device. |
| [KsValidateAllocatorCreateRequest function](..\ks\nf-ks-ksvalidateallocatorcreaterequest.md) | The KsValidateAllocatorCreateRequest function validates an IRP_MJ_CREATE request as an allocator request and returns the create structure associated with the request on success. |
| [KsDiscard function](..\ks\nf-ks-ksdiscard.md) | The KsDiscard macro removes a given item from an object bag. |
| [KsRemoveSpecificIrpFromCancelableQueue function](..\ks\nf-ks-ksremovespecificirpfromcancelablequeue.md) | The KsRemoveSpecificIrpFromCancelableQueue function removes the specified IRP from the specified queue. This is performed on an IRP that was previously acquired using KsRemoveIrpFromCancelableQueue, but that was not actually removed from the queue. |
| [KsRemoveIrpFromCancelableQueue function](..\ks\nf-ks-ksremoveirpfromcancelablequeue.md) | The KsRemoveIrpFromCancelableQueue function pops the next noncanceled IRP from the specified queue that can be canceled and removes its cancel status. |
| [KsFilterFactoryGetFirstChildFilter function](..\ks\nf-ks-ksfilterfactorygetfirstchildfilter.md) | The KsFilterFactoryGetFirstChildFilter function returns the first instantiated filter created by FilterFactory. |
| [KsStreamPointerAdvanceOffsets function](..\ks\nf-ks-ksstreampointeradvanceoffsets.md) | The KsStreamPointerAdvanceOffsets function advances the offsets of StreamPointer. |
| [KsPinSetPinClockTime function](..\ks\nf-ks-kspinsetpinclocktime.md) | The KsPinSetPinClockTime function sets the current time on the clock exposed by Pin. |
| [KsGetFilterFromIrp function](..\ks\nf-ks-ksgetfilterfromirp.md) | The KsGetFilterFromIrp function returns the AVStream filter object associated with a given IRP. |
| [IKsControl::KsMethod method](..\ks\nf-ks-ikscontrol-ksmethod.md) | The IKsControl |
| [KsPinRegisterIrpCompletionCallback function](..\ks\nf-ks-kspinregisterirpcompletioncallback.md) | The KsPinRegisterIrpCompletionCallback function registers a minidriver-defined callback routine for a specified pin. |
| [KsPinGetConnectedFilterInterface function](..\ks\nf-ks-kspingetconnectedfilterinterface.md) | The KsPinGetConnectedFilterInterface function queries the filter to which Pin is connected in order to obtain a pointer to a COM interface. |
| [KsPinGetConnectedPinDeviceObject function](..\ks\nf-ks-kspingetconnectedpindeviceobject.md) | The KsPinGetConnectedPinDeviceObject function returns the device object at the top of the device stack corresponding to the sink pin attached to the source pin Pin. |
| [KsCreateDefaultAllocatorEx function](..\ks\nf-ks-kscreatedefaultallocatorex.md) | Creates a default allocator that uses the specified memory pool and associates the IoGetCurrentIrpStackLocation(pIrp)-&gt;FileObject with this allocator using an internal dispatch table (KSDISPATCH_TABLE). |
| [KsCreateClock function](..\ks\nf-ks-kscreateclock~r1.md) | The KsCreateClock function creates a handle to a clock instance. |
| [KsAddObjectCreateItemToObjectHeader function](..\ks\nf-ks-ksaddobjectcreateitemtoobjectheader.md) | The KsAddObjectCreateItemToObjectHeader function adds the specified create-item to an empty item in the previously allocated create item list for this object header. |
| [IKsReferenceClock::GetTime method](..\ks\nf-ks-iksreferenceclock-gettime.md) | The IKsReferenceClock |
| [KsGateRemoveOnInputFromAnd function](..\ks\nf-ks-ksgateremoveoninputfromand.md) | The KsGateRemoveOnInputFromAnd function removes an existing input that is in the ON state from an AND gate. |
| [KsMethodHandler function](..\ks\nf-ks-ksmethodhandler.md) | The KsMethodHandler function handles methods requested through IOCTL_KS_METHOD. It works with all method identifiers defined by the sets. The function can only be called at PASSIVE_LEVEL. |
| [KsSetMajorFunctionHandler function](..\ks\nf-ks-kssetmajorfunctionhandler.md) | The KsSetMajorFunctionHandler function sets the handler for a specified major function to use the internal dispatching. |
| [KsReleaseCachedMdl function](..\ks\nf-ks-ksreleasecachedmdl.md) | The KsReleaseCachedMdl function is used to release the MDL acquired by the KsAcquireCachedMdl call. |
| [KsPinRegisterHandshakeCallback function](..\ks\nf-ks-kspinregisterhandshakecallback.md) | The KsPinRegisterHandshakeCallback function registers a minidriver-provided callback routine for a given pin. |
| [KsFilterGetOuterUnknown function](..\ks\nf-ks-ksfiltergetouterunknown.md) | The KsFilterGetOuterUnknown function returns the outer IUnknown interface of the filter specified by Filter. |
| [KsCreateTopologyNode function](..\ks\nf-ks-kscreatetopologynode~r1.md) | The KsCreateTopologyNode function creates a handle to a topology node instance. The function can only be called at PASSIVE_LEVEL. |
| [KsPinRegisterAggregatedClientUnknown function](..\ks\nf-ks-kspinregisteraggregatedclientunknown.md) | This inline function is a wrapper for KsRegisterAggregatedClientUnknown. |
| [KsGetPinFromIrp function](..\ks\nf-ks-ksgetpinfromirp.md) | The KsGetPinFromIrp function returns the AVStream pin object associated with the given IRP. |
| [KsAddIrpToCancelableQueue function](..\ks\nf-ks-ksaddirptocancelablequeue.md) | The KsAddIrpToCancelableQueue function adds an IRP to a queue of cancelable IRPs, thus allowing the IRP to be canceled. If the IRP had been previously set to a canceled state, the KsAddIrpToCancelableQueue function completes the canceling of that IRP. |
| [KsGateAddOffInputToOr function](..\ks\nf-ks-ksgateaddoffinputtoor.md) | The KsGateAddOffInputToOr function adds a new input in the OFF state to a given OR gate. |
| [KsDiscardEvent function](..\ks\nf-ks-ksdiscardevent.md) | The KsDiscardEvent function discards the memory used by an event entry after the objects have been dereferenced. |
| [KsFilterGetChildPinCount function](..\ks\nf-ks-ksfiltergetchildpincount.md) | The KsFilterGetChildPinCountfunctionreturns the number of pins of a given type that are currently instantiated on a given filter. |
| [KsGetFirstChild function](..\ks\nf-ks-ksgetfirstchild.md) | The KsGetFirstChild function returns the first AVStream child object of Object. |
| [IKsReferenceClock::GetResolution method](..\ks\nf-ks-iksreferenceclock-getresolution.md) | The IKsReferenceClock |
| [KsPinAttachAndGate function](..\ks\nf-ks-kspinattachandgate.md) | The KsPinAttachAndGate function connects Pin as an input to a previously initialized AND gate, and connects AndGate as an input to the relevant filter's AND gate. |
| [KsDisableEvent function](..\ks\nf-ks-ksdisableevent.md) | The KsDisableEvent function disables events requested through IOCTL_KS_DISABLE_EVENT. |
| [KsProbeStreamIrp function](..\ks\nf-ks-ksprobestreamirp.md) | The KsProbeStreamIrp function makes the specified modifications to the input and output buffers of the given IRP based on the flags passed, and it then validates the stream header. |
| [KsFilterReleaseProcessingMutex function](..\ks\nf-ks-ksfilterreleaseprocessingmutex.md) | The KsFilterReleaseProcessingMutex function releases the processing mutex for the AVStream filter specified by Filter. |
| [KsRegisterAggregatedClientUnknown function](..\ks\nf-ks-ksregisteraggregatedclientunknown.md) | In a manner very similar to COM, the KsRegisterAggregatedClientUnknown function aggregates two objects |
| [KsPinGetDevice function](..\ks\nf-ks-kspingetdevice.md) | The KsPinGetDevice function returns the AVStream device to which Pin belongs. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [KSGRAPHMANAGER_FUNCTIONTABLE structure](..\ks\ns-ks-ksgraphmanager-functiontable.md) | TBD. |
| [PKSPROPERTY_ITEM structure](..\ks\ns-ks-pksproperty-item.md) | Drivers use the KSPROPERTY_ITEM structure to describe how they support a property in a property set. |
| [PKS_FRAMING_RANGE_WEIGHTED structure](..\ks\ns-ks-pks-framing-range-weighted.md) | Drivers can use the KS_FRAMING_RANGE_WEIGHTED structure to specify a range of weighted frame sizes. |
| [PKSPROPERTY_MEDIAAVAILABLE structure](..\ks\ns-ks-pksproperty-mediaavailable.md) | The KSPROPERTY_MEDIAAVAILABLE structure specifies the media time span (the time span that a client can seek within) that is currently available on a filter. |
| [PKSOBJECT_CREATE structure](..\ks\ns-ks-pksobject-create.md) | The KSOBJECT_CREATE structure contains an array of create handlers for base object classes supported by this device object. |
| [PKSPIN_PHYSICALCONNECTION structure](..\ks\ns-ks-pkspin-physicalconnection.md) | A structure of type KSPIN_PHYSICALCONNECTION is returned in response to a KSPROPERTY_PIN_PHYSICALCONNECTION request. |
| [PKS_FRAMING_ITEM structure](..\ks\ns-ks-pks-framing-item.md) | The KS_FRAMING_ITEM structure is used to declare allocator requirements on a kernel-mode pin. |
| [PKSPROPERTY_POSITIONS structure](..\ks\ns-ks-pksproperty-positions.md) | The KSPROPERTY_POSITIONS structure specifies the current position and stop position, relative to the total duration of the stream. |
| [PKSDPC_ITEM structure](..\ks\ns-ks-pksdpc-item.md) | The KSDPC_ITEM structure is used to store information related to any internal DPCs that might be used to generate event notification from a raised IRQL. |
| [PKSIDENTIFIER structure](..\ks\ns-ks-pksidentifier.md) | The KSIDENTIFIER structure specifies a GUID that uniquely identifies a related set of GUIDs, and an index value to refer to a specific member within that set. |
| [PKSQUERYBUFFER structure](..\ks\ns-ks-pksquerybuffer.md) | The KSQUERYBUFFER structure is used when querying for outstanding buffers available on an event with KSEVENT_TYPE_QUERYBUFFER. |
| [PKSP_PIN structure](..\ks\ns-ks-pksp-pin.md) | Kernel streaming clients use the KSP_PIN structure to specify the property and pin type within a KSPROPSETID_Pin property request. |
| [PKSTOPOLOGY_CONNECTION structure](..\ks\ns-ks-pkstopology-connection.md) | The KSTOPOLOGY_CONNECTION structure describes a single data-path connection inside a kernel streaming filter. |
| [PKSPROPERTY_SERIAL structure](..\ks\ns-ks-pksproperty-serial.md) | The KSPROPERTY_SERIAL structure is a header that is included for each property that follows a KSPROPERTY_SERIALHDR structure. |
| [PKSMETHOD_SET structure](..\ks\ns-ks-pksmethod-set.md) | The KSMETHOD_SET structure describes the methods that comprise a kernel streaming method set. |
| [PKSNODE_CREATE structure](..\ks\ns-ks-pksnode-create.md) | The KSNODE_CREATE structure describes the set of information used to create the node handle. |
| [PKSPIN_MDL_CACHING_NOTIFICATION32 structure](..\ks\ns-ks-pkspin-mdl-caching-notification32.md) | This structure is used internally by the operating system. |
| [PKSHANDSHAKE structure](..\ks\ns-ks-pkshandshake.md) | The KSHANDSHAKE structure is used to pass information back and forth while pins are handshaking in an attempt to negotiate a private interface. |
| [PKSSTREAMALLOCATOR_STATUS_EX structure](..\ks\ns-ks-pksstreamallocator-status-ex.md) | Client use KSSTREAMALLOCATOR_STATUS_EX to query the status for allocators supporting the extended allocator framing. |
| [PKSFASTPROPERTY_ITEM structure](..\ks\ns-ks-pksfastproperty-item.md) | The KSFASTPROPERTY_ITEM structure is used with items for fast I/O dispatching. |
| [PKSPROPERTY_VALUES structure](..\ks\ns-ks-pksproperty-values.md) | The KSPROPERTY_VALUES structure describes the type and acceptable default values of a property. |
| [PKSPROPERTY_BOUNDS_LONGLONG structure](..\ks\ns-ks-pksproperty-bounds-longlong.md) | The KSPROPERTY_BOUNDS_LONGLONG structure defines the bounds for a 64-bit property. |
| [PKSPROPERTY_STEPPING_LONGLONG structure](..\ks\ns-ks-pksproperty-stepping-longlong.md) | The KSPROPERTY_STEPPING_LONGLONG structure defines the valid range of values for a 64-bit property. |
| [PKSPIN_MDL_CACHING_NOTIFICATION structure](..\ks\ns-ks-pkspin-mdl-caching-notification.md) | This structure is used internally by the operating system. |
| [PKSCLOCK_CREATE structure](..\ks\ns-ks-pksclock-create.md) | The KSCLOCK_CREATE structure is used in clock create parameters for the KsCreateClock function. |
| [PKSE_NODE structure](..\ks\ns-ks-pkse-node.md) | The KSE_NODE structure specifies an event request on a specific node. |
| [PKSINTERVAL structure](..\ks\ns-ks-pksinterval.md) | The KSINTERVAL structure specifies a base time and time interval for recurring events. |
| [PKS_COMPRESSION structure](..\ks\ns-ks-pks-compression.md) | The KS_COMPRESSION structure defines the compression of frames on an output pin. |
| [PKSPROPERTY_SET structure](..\ks\ns-ks-pksproperty-set.md) | A kernel streaming driver or pin may use the KSPROPERTY_SET structure to describe how it supports a property set. |
| [MF_MDL_SHARED_PAYLOAD_KEY structure](..\ks\ns-ks--mf-mdl-shared-payload-key.md) | This union is used internally by the operating system. |
| [PKSPIN_CONNECT structure](..\ks\ns-ks-pkspin-connect.md) | Clients use the KSPIN_CONNECT structure to describe the connection they request from a driver in a KsCreatePin call. |
| [PKSPIN_DESCRIPTOR structure](..\ks\ns-ks-pkspin-descriptor.md) | The KSPIN_DESCRIPTOR structure describes the basic KSPROPSETID_Pin properties of a pin type. |
| [PKSPROPERTY_MEMBERSLIST structure](..\ks\ns-ks-pksproperty-memberslist.md) | The KSPROPERTY_MEMBERSLIST structure contains a list of legal values or ranges for a property. |
| [PKSRESOLUTION structure](..\ks\ns-ks-pksresolution.md) | The KSRESOLUTION structure specifies granularity and error of a kernel streaming clock. |
| [PKSALLOCATOR_FRAMING_EX structure](..\ks\ns-ks-pksallocator-framing-ex.md) | The KSALLOCATOR_FRAMING_EX structure is the AVStream replacement for KSALLOCATOR_FRAMING. KSALLOCATOR_FRAMING_EX defines allocator requirements on a pin in a kernel level filter. |
| [PKSQUALITY structure](..\ks\ns-ks-pksquality.md) | The KSQUALITY structure is used to report QM problems in both kernel and user mode to their respective quality managers. |
| [PKSE_PIN structure](..\ks\ns-ks-pkse-pin.md) | TBD. |
| [PKSPROPERTY_BOUNDS_LONG structure](..\ks\ns-ks-pksproperty-bounds-long.md) | The KSPROPERTY_BOUNDS_LONG structure defines the bounds for a 32-bit property. |
| [PKSEVENT_ITEM structure](..\ks\ns-ks-pksevent-item.md) | The KSEVENT_ITEM structure describe a minidriver's support for a specific event within an event set. |
| [PKSPROPERTY_MEMBERSHEADER structure](..\ks\ns-ks-pksproperty-membersheader.md) | A driver provides a structure of type KSPROPERTY_MEMBERSHEADER to describe the size and type of each element in an array containing property values or ranges. |
| [PKSDISPATCH_TABLE structure](..\ks\ns-ks-pksdispatch-table.md) | The KSDISPATCH_TABLE structure contains pointers to minidriver implemented IRP dispatch routines. |
| [PKSM_NODE structure](..\ks\ns-ks-pksm-node.md) | Just as KSP_NODE is used for properties on a node, the KSM_NODE structure is used for methods on a node. |
| [PKSCOMPONENTID structure](..\ks\ns-ks-pkscomponentid.md) | The KSCOMPONENTID structure contains unique identifiers that describe an individual kernel streaming object. |
| [PKSP_NODE structure](..\ks\ns-ks-pksp-node.md) | Kernel streaming clients use the KSP_NODE structure to specify the property and node type within a KSPROPERTY_TOPOLOGY_NAME property request. |
| [PKSBUFFER_ITEM structure](..\ks\ns-ks-pksbuffer-item.md) | The KSBUFFER_ITEM structure is used to store a list of data buffers copied from the event source, which can be retrieved by the event sink through KSEVENT_TYPE_QUERYBUFFER. |
| [PBUS_INTERFACE_REFERENCE structure](..\ks\ns-ks-pbus-interface-reference.md) | A software device enumerator exports this interface to allow drivers to reference count physical device objects (PDOs) such that the device remains active while in use and is unloaded when not in use. |
| [PKSCLOCK_FUNCTIONTABLE structure](..\ks\ns-ks-pksclock-functiontable.md) | The KSCLOCK_FUNCTIONTABLE structure describes a function table for the master clock. |
| [PKSFASTMETHOD_ITEM structure](..\ks\ns-ks-pksfastmethod-item.md) | Drivers provide a structure of type KSFASTMETHOD_ITEM to support fast I/O dispatching. |
| [PKSDATARANGE structure](..\ks\ns-ks-pksdatarange.md) | The KSDATARANGE structure is a variable-length structure that describes a range of data formats. |
| [PKSPROPERTY_DESCRIPTION structure](..\ks\ns-ks-pksproperty-description.md) | The KSPROPERTY_DESCRIPTION structure specifies the size and type of values contained in a specific property. |
| [KSPROPERTY_GRAPHMANAGER_INTERFACE structure](..\ks\ns-ks--ksproperty-graphmanager-interface.md) | TBD. |
| [PKSALLOCATOR_FRAMING structure](..\ks\ns-ks-pksallocator-framing.md) | The KSALLOCATOR_FRAMING structure is used to query framing requirements and submit allocator creation requests. |
| [PKSDATARANGE structure](..\ks\ns-ks-pksdatarange~r1.md) | The KSDATARANGE structure is a variable-length structure that describes a range of data formats. |
| [PKSPROPERTY_SERIALHDR structure](..\ks\ns-ks-pksproperty-serialhdr.md) | The format of the serialization buffer is a KSPROPERTY_SERIALHDR structure, followed by serialized properties. |
| [PKSRATE structure](..\ks\ns-ks-pksrate.md) | The query is passed a KSRATE structure appended to the property containing the rate request (known as a KSRATE_CAPABILITY structure), and is returned a KSRATE structure filled in with the capability given the rate request. |
| [PKSRATE_CAPABILITY structure](..\ks\ns-ks-pksrate-capability.md) | The client uses the KSRATE_CAPABILITY structure in a KSPROPERTY_STREAM_RATECAPABILITY property request. |
| [PKSEVENT_TIME_INTERVAL structure](..\ks\ns-ks-pksevent-time-interval.md) | The KSEVENT_TIME_INTERVAL structure is used in various events within the KSEVENTSETID_Clock event set. |
| [PKSPRIORITY structure](..\ks\ns-ks-pkspriority.md) | The KSPRIORITY structure is used to specify priority and is used with the KSPROPERTY_CONNECTION_PRIORITY property. |
| [PKSSTREAM_UVC_METADATA structure](..\ks\ns-ks-pksstream-uvc-metadata.md) | The KSSTREAM_UVC_METADATA structure contains start and end of frame timestamp information. |
| [PKSSTREAMALLOCATOR_FUNCTIONTABLE structure](..\ks\ns-ks-pksstreamallocator-functiontable.md) | Clients can request the function table of a given allocator by sending a KSSTREAMALLOCATOR_FUNCTIONTABLE structure in a KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE property request. |
| [PKSEVENT_SET structure](..\ks\ns-ks-pksevent-set.md) | The KSEVENT_SET structure describes the events that comprise a kernel streaming event set. |
| [PKSPROPERTY_STEPPING_LONG structure](..\ks\ns-ks-pksproperty-stepping-long.md) | The KSPROPERTY_STEPPING_LONG structure defines the valid range of values for a 32-bit property. |
| [PKSSTREAM_METADATA_INFO structure](..\ks\ns-ks-pksstream-metadata-info.md) | This structure contains the metadata information that is passed down to the driver. |
| [PKSSTREAM_UVC_METADATATYPE_TIMESTAMP structure](..\ks\ns-ks-pksstream-uvc-metadatatype-timestamp.md) | The KSSTREAM_UVC_METADATATYPE_TIMESTAMP structure contains USB video class (UVC) clock and timestamp information. |
| [PKSEVENTDATA structure](..\ks\ns-ks-pkseventdata.md) | Kernel streaming clients send the KSEVENTDATA structure to the class driver to specify a notification method. |
| [PKSMULTIPLE_ITEM structure](..\ks\ns-ks-pksmultiple-item.md) | The KSMULTIPLE_ITEM structure is a generic header for property data that can contain multiple entries. |
| [KSDEVICE_THERMAL_DISPATCH structure](..\ks\ns-ks--ksdevice-thermal-dispatch.md) | The KSDEVICE_THERMAL_DISPATCH structure is used by the miniport driver in the API call to register thermal notification callbacks. This structure contains the callback function pointers for active and passive cooling interfaces. |
| [PKSCORRELATED_TIME structure](..\ks\ns-ks-pkscorrelated-time.md) | The KSCORRELATED_TIME structure contains a clock time as well as the corresponding number of clock ticks since system boot. |
| [PKSSTREAMALLOCATOR_STATUS structure](..\ks\ns-ks-pksstreamallocator-status.md) | The KSSTREAMALLOCATOR_STATUS structure describes framing requirements and current number of allocated frames for a specific allocator. |
| [PKSATTRIBUTE_LIST structure](..\ks\ns-ks-pksattribute-list.md) | The KSATTRIBUTE_LIST structure contains an attribute defined in a KSATTRIBUTE structure. |
| [PKSATTRIBUTE structure](..\ks\ns-ks-pksattribute.md) | The KSATTRIBUTE structure defines an additional attribute of a data format or data range that is not covered by the KSDATAFORMAT and KSDATARANGE structures or the extended information based on the format and range specifiers. |
| [PKSFRAMETIME structure](..\ks\ns-ks-pksframetime.md) | The KSFRAMETIME structure is supported by rendering pins, and is used to return the duration of the next &#0034;frame&#0034; of data, and flags associated with that frame. |
| [PKSOBJECT_CREATE_ITEM structure](..\ks\ns-ks-pksobject-create-item.md) | The KSOBJECT_CREATE_ITEM structure is used to look up the string passed to a create request. |
| [PKSTOPOLOGY structure](..\ks\ns-ks-pkstopology.md) | The KSTOPOLOGY structure describes the topology of pins and nodes. |
| [PKS_FRAMING_RANGE structure](..\ks\ns-ks-pks-framing-range.md) | The KS_FRAMING_RANGE structure specifies a range for frame sizes for a given framing item. |
| [PKSSTREAM_HEADER structure](..\ks\ns-ks-pksstream-header.md) | The KSSTREAM_HEADER structure is a variable-length structure that describes a packet of data to be read from or written to a streaming driver pin. |
| [PKSP_TIMEFORMAT structure](..\ks\ns-ks-pksp-timeformat.md) | The KSP_TIMEFORMAT structure corresponds to KSPROPERTY_MEDIASEEKING_CONVERTTIMEFORMAT. |
| [PKSERROR structure](..\ks\ns-ks-pkserror.md) | The KSERROR structure is used to report streaming errors in both kernel and user mode to their respective quality managers. |
| [PKSTIME structure](..\ks\ns-ks-pkstime.md) | The KSTIME structure specifies a time stamp that can be used to indicate stream position. |
| [PKSEVENT_TIME_MARK structure](..\ks\ns-ks-pksevent-time-mark.md) | The KSEVENT_TIME_MARK structure is used in various events within the KSEVENTSETID_Clock event set. |
| [PBUS_INTERFACE_MEDIUMS structure](..\ks\ns-ks-pbus-interface-mediums.md) | TBD. |
| [PKSPIN_CINSTANCES structure](..\ks\ns-ks-pkspin-cinstances.md) | TBD. |
| [PKSMETHOD_ITEM structure](..\ks\ns-ks-pksmethod-item.md) | The KSMETHOD_ITEM structure describes a single method within a method set. |
| [PKSQUALITY_MANAGER structure](..\ks\ns-ks-pksquality-manager.md) | The KSQUALITY_MANAGER structure is used with the KSPROPERTY_STREAM_QUALITY property and contains the handle of the quality manager sink and a context to pass in the quality complaints. |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IKsControl interface](..\ks\nn-ks-ikscontrol~r1.md) | The IKsControl interface is a COM-style interface implemented on AVStream filters and pins. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [KSPROPERTY_SERVICE enumeration](..\ksi\ne-ksi-ksproperty-service.md) | TBD. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PKSCLOCKINSTANCE structure](..\ksi\ns-ksi-pksclockinstance.md) | TBD. |
| [PKSIDEFAULTCLOCK structure](..\ksi\ns-ksi-pksidefaultclock.md) | TBD. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IKsClockPropertySet::KsGetTime method](..\ksproxy\nf-ksproxy-iksclockpropertyset-ksgettime.md) | The KsGetTime method retrieves the time of the underlying clock. |
| [IKsDataTypeHandler::KsPrepareIoOperation method](..\ksproxy\nf-ksproxy-iksdatatypehandler-ksprepareiooperation.md) | The KsPrepareIoOperation method initializes the extended header and prepares the media sample for an I/O operation. |
| [IKsPin::KsQueryInterfaces method](..\ksproxy\nf-ksproxy-ikspin-ksqueryinterfaces.md) | The KsQueryInterfaces method retrieves interfaces that a pin supports. |
| [IKsPropertySet::QuerySupported method](..\ksproxy\nf-ksproxy-ikspropertyset-querysupported.md) | The QuerySupported method determines whether a KS object supports a property set and the type of that support. |
| [IKsPin::KsIncrementPendingIoCount method](..\ksproxy\nf-ksproxy-ikspin-ksincrementpendingiocount.md) | The KsIncrementPendingIoCount method increments the number of input/output (I/O) operations that are in progress on a pin. |
| [IKsClockPropertySet::KsGetCorrelatedPhysicalTime method](..\ksproxy\nf-ksproxy-iksclockpropertyset-ksgetcorrelatedphysicaltime.md) | The KsGetCorrelatedPhysicalTime method retrieves the physical time and the correlated system time from the underlying clock. |
| [IKsInterfaceHandler::KsProcessMediaSamples method](..\ksproxy\nf-ksproxy-iksinterfacehandler-ksprocessmediasamples.md) | The KsProcessMediaSamples method processes media samples. |
| [IKsPin::KsPeekAllocator method](..\ksproxy\nf-ksproxy-ikspin-kspeekallocator.md) | The KsPeekAllocator method returns a pointer to an IMemAllocator interface for a pin's assigned allocator. |
| [IKsClockPropertySet::KsSetCorrelatedPhysicalTime method](..\ksproxy\nf-ksproxy-iksclockpropertyset-kssetcorrelatedphysicaltime.md) | The KsSetCorrelatedPhysicalTime method sets the physical time with the correlated system time on the underlying clock. |
| [IKsPinFactory::KsPinFactory method](..\ksproxy\nf-ksproxy-ikspinfactory-kspinfactory.md) | The KsPinFactory method retrieves the identifier of a pin factory. |
| [IKsQualityForwarder::KsFlushClient method](..\ksproxy\nf-ksproxy-iksqualityforwarder-ksflushclient.md) | The KsFlushClient method flushes information from a pin. |
| [IKsInterfaceHandler::KsSetPin method](..\ksproxy\nf-ksproxy-iksinterfacehandler-kssetpin.md) | The KsSetPin method informs the streaming interface handler about the pin with which to communicate when passing data. |
| [KsOpenDefaultDevice function](..\ksproxy\nf-ksproxy-ksopendefaultdevice.md) | The KsOpenDefaultDevice function opens a handle to the first device that is listed in the specified Plug and Play (PnP) category. |
| [IKsPin::KsQueryMediums method](..\ksproxy\nf-ksproxy-ikspin-ksquerymediums.md) | The KsQueryMediums method retrieves mediums that a pin supports. |
| [IKsPin::KsGetCurrentCommunication method](..\ksproxy\nf-ksproxy-ikspin-ksgetcurrentcommunication.md) | The KsGetCurrentCommunication method retrieves the current communication direction, interface, and medium of a pin. |
| [IKsPin::KsDecrementPendingIoCount method](..\ksproxy\nf-ksproxy-ikspin-ksdecrementpendingiocount.md) | The KsDecrementPendingIoCount method decrements the number of input/output (I/O) operations that are in progress on a pin. |
| [IKsPin::KsPropagateAcquire method](..\ksproxy\nf-ksproxy-ikspin-kspropagateacquire.md) | The KsPropagateAcquire method directs all the pins on the filter to attain the Acquire state. |
| [IKsClockPropertySet::KsGetCorrelatedTime method](..\ksproxy\nf-ksproxy-iksclockpropertyset-ksgetcorrelatedtime.md) | The KsGetCorrelatedTime method retrieves the current time and the correlated system time from the underlying clock. |
| [IKsClockPropertySet::KsSetTime method](..\ksproxy\nf-ksproxy-iksclockpropertyset-kssettime.md) | The KsSetTime method sets the current time on the underlying clock. |
| [IKsObject::KsGetObjectHandle method](..\ksproxy\nf-ksproxy-iksobject-ksgetobjecthandle.md) | The KsGetObjectHandle method retrieves a file handle to a KS object. |
| [IKsClockPropertySet::KsSetCorrelatedTime method](..\ksproxy\nf-ksproxy-iksclockpropertyset-kssetcorrelatedtime.md) | The KsSetCorrelatedTime method sets the current time with the correlated system time on the underlying clock. |
| [IKsControl::KsEvent method](..\ksproxy\nf-ksproxy-ikscontrol-ksevent.md) | The KsEvent method enables or disables an event, along with any other defined support operations available on an event set. |
| [IKsControl::KsProperty method](..\ksproxy\nf-ksproxy-ikscontrol-ksproperty.md) | The KsProperty method sets a property or retrieves property information, along with any other defined support operations available on a property set. |
| [IKsInterfaceHandler::KsCompleteIo method](..\ksproxy\nf-ksproxy-iksinterfacehandler-kscompleteio.md) | The KsCompleteIo method cleans up extended headers and releases media samples after input and output (I/O) complete. |
| [IKsClockPropertySet::KsGetState method](..\ksproxy\nf-ksproxy-iksclockpropertyset-ksgetstate.md) | The KsGetState method retrieves the streaming state of a pin from the underlying clock. |
| [IKsPin::KsDeliver method](..\ksproxy\nf-ksproxy-ikspin-ksdeliver.md) | The KsDeliver method delivers a media sample from an output pin to an input pin, continues an I/O operation by retrieving the next buffer from an allocator, and submits the buffer to the associated device. |
| [IKsPin::KsMediaSamplesCompleted method](..\ksproxy\nf-ksproxy-ikspin-ksmediasamplescompleted.md) | The KsMediaSamplesCompleted method informs a pin that a stream segment completed. |
| [IKsPinEx::KsNotifyError method](..\ksproxy\nf-ksproxy-ikspinex-ksnotifyerror.md) | The KsNotifyError method notifies the filter graph of an error to give the filter graph an opportunity to halt. |
| [IKsControl::KsMethod method](..\ksproxy\nf-ksproxy-ikscontrol-ksmethod.md) | The KsMethod method sends a method to a KS object, along with any other defined support operations available on a method set. |
| [KsGetMediaType function](..\ksproxy\nf-ksproxy-ksgetmediatype.md) | The KsGetMediaType function retrieves information about a media type on a pin factory identifier. |
| [IKsPropertySet::Get method](..\ksproxy\nf-ksproxy-ikspropertyset-get.md) | The Get method retrieves a property identified by a property-set GUID and a property identifier. |
| [KsSynchronousDeviceControl function](..\ksproxy\nf-ksproxy-kssynchronousdevicecontrol.md) | The KsSynchronousDeviceControl function issues a synchronous device I/O control operation to the KS object that is specified by a file handle. |
| [IKsAggregateControl::KsAddAggregate method](..\ksproxy\nf-ksproxy-iksaggregatecontrol-ksaddaggregate.md) | The KsAddAggregate method adds a COM server as an aggregate provider to the list of interface providers for the KS object that exposes the IKsAggregateControl interface. |
| [IKsClockPropertySet::KsGetResolution method](..\ksproxy\nf-ksproxy-iksclockpropertyset-ksgetresolution.md) | The KsGetResolution method retrieves the clock resolution from the underlying clock. |
| [KsGetMediaTypeCount function](..\ksproxy\nf-ksproxy-ksgetmediatypecount.md) | The KsGetMediaTypeCount function returns the number of available media types on a pin factory identifier. |
| [IKsDataTypeCompletion::KsCompleteMediaType method](..\ksproxy\nf-ksproxy-iksdatatypecompletion-kscompletemediatype.md) | The KsCompleteMediaType method completes a partially-specified media type that was first presented to the IAMStreamConfig |
| [KsGetMultiplePinFactoryItems function](..\ksproxy\nf-ksproxy-ksgetmultiplepinfactoryitems.md) | The KsGetMultiplePinFactoryItems function retrieves pin property items in a variable length data buffer. |
| [IKsAggregateControl::KsRemoveAggregate method](..\ksproxy\nf-ksproxy-iksaggregatecontrol-ksremoveaggregate.md) | The KsRemoveAggregate method removes a previously added COM server aggregate provider from the list of interface providers for the KS object that exposes the IKsAggregateControl interface. |
| [IKsDataTypeHandler::KsSetMediaType method](..\ksproxy\nf-ksproxy-iksdatatypehandler-kssetmediatype.md) | The KsSetMediaType method sets the media type for a data type handler. |
| [IKsNotifyEvent::KsNotifyEvent method](..\ksproxy\nf-ksproxy-iksnotifyevent-ksnotifyevent.md) | The KsNotifyEvent method requests that the KS object that owns the given DirectShow event notify the calling application with the given parameters whenever action related to the event occurs. |
| [IKsPin::KsCreateSinkPinHandle method](..\ksproxy\nf-ksproxy-ikspin-kscreatesinkpinhandle.md) | The KsCreateSinkPinHandle method creates a pin handle and stores it in the KS pin object. |
| [IKsClockPropertySet::KsGetPhysicalTime method](..\ksproxy\nf-ksproxy-iksclockpropertyset-ksgetphysicaltime.md) | The KsGetPhysicalTime method retrieves the physical time from the underlying clock. |
| [IKsClockPropertySet::KsSetPhysicalTime method](..\ksproxy\nf-ksproxy-iksclockpropertyset-kssetphysicaltime.md) | The KsSetPhysicalTime method sets the physical time on the underlying clock. |
| [IKsTopology::CreateNodeInstance method](..\ksproxy\nf-ksproxy-ikstopology-createnodeinstance.md) | The CreateNodeInstance method requests a KS filter object to open a topology node object. |
| [KsResolveRequiredAttributes function](..\ksproxy\nf-ksproxy-ksresolverequiredattributes.md) | The KsResolveRequiredAttributes function searches the attributes list that is attached to a data range for specified attributes and ensures that all specified attributes were found. |
| [IKsDataTypeHandler::KsQueryExtendedSize method](..\ksproxy\nf-ksproxy-iksdatatypehandler-ksqueryextendedsize.md) | The KsQueryExtendedSize method retrieves extended header information required for input and output (I/O) operations. |
| [IKsPropertySet::Set method](..\ksproxy\nf-ksproxy-ikspropertyset-set.md) | The Set method sets a property identified by a property-set GUID and a property identifier. |
| [IKsDataTypeHandler::KsCompleteIoOperation method](..\ksproxy\nf-ksproxy-iksdatatypehandler-kscompleteiooperation.md) | The KsCompleteIoOperation method cleans up the extended header and completes the input and output (I/O) operation. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [KSALLOCATORMODE enumeration](..\ksproxy\ne-ksproxy-ksallocatormode.md) | TBD. |
| [FRAMING_PROP enumeration](..\ksproxy\ne-ksproxy-framing-prop.md) | TBD. |
| [FRAMING_CACHE_OPS enumeration](..\ksproxy\ne-ksproxy-framing-cache-ops.md) | TBD. |
| [PIPE_ALLOCATOR_PLACE enumeration](..\ksproxy\ne-ksproxy-pipe-allocator-place.md) | TBD. |
| [KSPEEKOPERATION enumeration](..\ksproxy\ne-ksproxy-kspeekoperation.md) | TBD. |
| [KSIOOPERATION enumeration](..\ksproxy\ne-ksproxy-ksiooperation.md) | TBD. |
| [PIPE_STATE enumeration](..\ksproxy\ne-ksproxy-pipe-state.md) | TBD. |
| [KS_LogicalMemoryType enumeration](..\ksproxy\ne-ksproxy-ks-logicalmemorytype.md) | TBD. |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IKsControl interface](..\ksproxy\nn-ksproxy-ikscontrol.md) | The IKsControl interface provides user-mode methods that control a KS filter or KS pin. See the IKsControl AVStream COM interface for information about the user-mode equivalent of this interface. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [OPTIMAL_WEIGHT_TOTALS structure](..\ksproxy\ns-ksproxy-optimal-weight-totals.md) | TBD. |
| [KSSTREAM_SEGMENT structure](..\ksproxy\ns-ksproxy--ksstream-segment~r1.md) | The KSSTREAM_SEGMENT structure contains information that describes an I/O operation occurring on a stream. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [LAMP_MODE enumeration](..\lamp\ne-lamp-lamp-mode.md) | This enumeration contains the operating modes of a lamp device. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [LAMP_INTENSITY_WHITE structure](..\lamp\ns-lamp-lamp-intensity-white.md) | This structure is the I/O parameter type of IOCTL_LAMP_GET_INTENSITY_WHITE and IOCTL_LAMP_SET_INTENSITY_WHITE. |
| [LAMP_CAPABILITIES_COLOR structure](..\lamp\ns-lamp-lamp-capabilities-color.md) | This structure is the I/O parameter type of IOCTL_LAMP_{GET|SET}_INTENSITY_COLOR. |
| [LAMP_INTENSITY_COLOR structure](..\lamp\ns-lamp-lamp-intensity-color.md) | This structure is the I/O parameter type of IOCTL_LAMP_GET_INTENSITY_COLOR and IOCTL_LAMP_SET_INTENSITY_COLOR. |
| [LAMP_CAPABILITIES_WHITE structure](..\lamp\ns-lamp-lamp-capabilities-white.md) | This structure is the I/O parameter type of IOCTL_LAMP_{GET|SET}_INTENSITY_WHITE. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [tagMetadataTimeStamps structure](..\mfapi\ns-mfapi-tagmetadatatimestamps.md) | The MetadataTimeStamps structure describes the blob format for the MF_CAPTURE_METADATA_FACEROITIMESTAMPS attribute. |
| [tagHistogramGrid structure](..\mfapi\ns-mfapi-taghistogramgrid.md) | The HistogramGrid structure describes the blob format for MF_CAPTURE_METADATA_HISTOGRAM. |
| [tagFaceCharacterization structure](..\mfapi\ns-mfapi-tagfacecharacterization.md) | The FaceCharacterization structure describes the blob format for the MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS attribute. |
| [tagHistogramBlobHeader structure](..\mfapi\ns-mfapi-taghistogramblobheader.md) | The HistogramBlobHeader structure describes the blob size and the number of histograms in the blob for the MF_CAPTURE_METADATA_HISTOGRAM attribute. |
| [tagHistogramHeader structure](..\mfapi\ns-mfapi-taghistogramheader.md) | The HistogramHeader structure describes the blob format for MF_CAPTURE_METADATA_HISTOGRAM. |
| [tagCapturedMetadataISOGains structure](..\mfapi\ns-mfapi-tagcapturedmetadataisogains.md) | The CapturedMetadataISOGains structure describes the blob format for MF_CAPTURE_METADATA_ISO_GAINS. |
| [tagHistogramDataHeader structure](..\mfapi\ns-mfapi-taghistogramdataheader.md) | The HistogramDataHeader structure describes the blob format for the MF_CAPTURE_METADATA_HISTOGRAM attribute. |
| [tagFaceRectInfo structure](..\mfapi\ns-mfapi-tagfacerectinfo.md) | The FaceRectInfo structure describes the blob format for the MF_CAPTURE_METADATA_FACEROIS attribute. |
| [tagFaceRectInfoBlobHeader structure](..\mfapi\ns-mfapi-tagfacerectinfoblobheader.md) | The FaceRectInfoBlobHeader structure describes the size and count information of the blob format for the MF_CAPTURE_METADATA_FACEROIS attribute. |
| [tagFaceCharacterizationBlobHeader structure](..\mfapi\ns-mfapi-tagfacecharacterizationblobheader.md) | The FaceCharacterizationBlobHeader structure describes the size and count information of the blob format for the MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS attribute. |
| [tagCapturedMetadataExposureCompensation structure](..\mfapi\ns-mfapi-tagcapturedmetadataexposurecompensation.md) | This structure contains blob information for the EV compensation feedback for the photo captured. |
| [tagCapturedMetadataWhiteBalanceGains structure](..\mfapi\ns-mfapi-tagcapturedmetadatawhitebalancegains.md) | This structure describes the blob format for the MF_CAPTURE_METADATA_WHITEBALANCE_GAINS attribute. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [MF_MEDIASOURCE_STATUS_INFO enumeration](..\mfidl\ne-mfidl-mf-mediasource-status-info.md) | TBD. |
| [MF_TRANSFER_VIDEO_FRAME_FLAGS enumeration](..\mfidl\ne-mfidl-mf-transfer-video-frame-flags.md) | TBD. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [tag_video_stream_init_parms structure](..\msviddrv\ns-msviddrv-tag-video-stream-init-parms.md) | TBD. |
| [tag_video_geterrortext_parms structure](..\msviddrv\ns-msviddrv-tag-video-geterrortext-parms.md) | TBD. |
| [tag_video_open_parms structure](..\msviddrv\ns-msviddrv-tag-video-open-parms.md) | TBD. |
| [tag_video_configure_parms structure](..\msviddrv\ns-msviddrv-tag-video-configure-parms.md) | TBD. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [STREAM_PRIORITY enumeration](..\strmini\ne-strmini--stream-priority.md) | TBD. |
| [STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE enumeration](..\strmini\ne-strmini--stream-minidriver-device-notification-type.md) | TBD. |
| [STREAM_DEBUG_LEVEL enumeration](..\strmini\ne-strmini-stream-debug-level.md) | The STREAM_DEBUG_LEVEL enumeration lists incrementally increasing levels of debugger output. |
| [TIME_FUNCTION enumeration](..\strmini\ne-strmini-time-function.md) | TBD. |
| [SRB_COMMAND enumeration](..\strmini\ne-strmini--srb-command.md) | TBD. |
| [STREAM_BUFFER_TYPE enumeration](..\strmini\ne-strmini-stream-buffer-type.md) | This enumeration defines the buffer types for StreamClassGetPhysicalAddress. |
| [STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE enumeration](..\strmini\ne-strmini--stream-minidriver-stream-notification-type.md) | TBD. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [StreamClassDeviceNotification function](..\strmini\nf-strmini-streamclassdevicenotification.md) | Minidrivers use the StreamClassDeviceNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred. |
| [StreamClassGetNextEvent function](..\strmini\nf-strmini-streamclassgetnextevent.md) | Minidrivers can use the StreamClassGetNextEvent routine to search the event queue of a device or of a particular stream. |
| [StreamClassReadWriteConfig function](..\strmini\nf-strmini-streamclassreadwriteconfig.md) | The StreamClassReadWriteConfig routine reads or writes configuration data for the minidriver's parent bus driver. |
| [StreamClassGetDmaBuffer function](..\strmini\nf-strmini-streamclassgetdmabuffer.md) | The StreamClassGetDmaBuffer routine returns a pointer to the DMA buffer that the class driver allocates for the minidriver. |
| [StreamClassDebugPrint function](..\strmini\nf-strmini-streamclassdebugprint.md) | In a checked build environment, the minidriver can use the StreamClassDebugPrint routine to print debug messages to the application window and to the Debugger Command window. |
| [StreamClassScheduleTimer function](..\strmini\nf-strmini-streamclassscheduletimer.md) | The minidriver calls the StreamClassScheduleTimer routine to schedule a timer, and to specify a routine that is called when the timer expires. |
| [StreamClassGetPhysicalAddress function](..\strmini\nf-strmini-streamclassgetphysicaladdress.md) | The StreamClassGetPhysicalAddress routine translates a virtual memory address to a physical memory address and locks the corresponding physical memory for a DMA operation. |
| [StreamClassDebugAssert function](..\strmini\nf-strmini-streamclassdebugassert.md) | A minidriver can use the StreamClassDebugAssert routine in a checked build environment to fail an assert, causing the stream class driver to output a debug message and break into the kernel debugger. |
| [StreamClassCompleteRequestAndMarkQueueReady function](..\strmini\nf-strmini-streamclasscompleterequestandmarkqueueready.md) | The StreamClassCompleteRequestAndMarkQueueReady routine completes a request, and signals the class driver that the minidriver is ready to receive a new request of the same type. |
| [StreamClassStreamNotification function](..\strmini\nf-strmini-streamclassstreamnotification.md) | Streams use the StreamClassStreamNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred. |
| [StreamClassCallAtNewPriority function](..\strmini\nf-strmini-streamclasscallatnewpriority.md) | The StreamClassCallAtNewPriority routine schedules a routine to be called at a different priority. |
| [StreamClassQueryMasterClockSync function](..\strmini\nf-strmini-streamclassquerymasterclocksync.md) | The minidriver may call the StreamClassQueryMasterClockSync routine to synchronously query a stream's master clock. |
| [StreamClassRegisterFilterWithNoKSPins function](..\strmini\nf-strmini-streamclassregisterfilterwithnokspins.md) | The StreamClassRegisterFilterWithNoKSPins routine is used to register filter drivers with Microsoft DirectShow that have no kernel streaming pins and, therefore, do not stream in kernel mode. |
| [StreamClassQueryMasterClock function](..\strmini\nf-strmini-streamclassquerymasterclock.md) | When the minidriver calls the StreamClassQueryMasterClock routine, the class driver queries the appropriate time value of the master clock asynchronously, and passes the result to the routine passed in the ClockCallbackRoutine parameter. |
| [StreamClassAbortOutstandingRequests function](..\strmini\nf-strmini-streamclassabortoutstandingrequests.md) | The StreamClassAbortOutstandingRequests routine aborts all outstanding requests, either to a particular stream, or to the entire driver. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [STREAM_TIME_REFERENCE structure](..\strmini\ns-strmini--stream-time-reference.md) | TBD. |
| [PORT_CONFIGURATION_INFORMATION structure](..\strmini\ns-strmini--port-configuration-information~r1.md) | PORT_CONFIGURATION_INFORMATION describes the hardware settings of a streaming minidriver's device. The class driver fills in most members with information provided by the operating system. |
| [HW_STREAM_REQUEST_BLOCK structure](..\strmini\ns-strmini--hw-stream-request-block.md) | The stream class driver uses the HW_STREAM_REQUEST_BLOCK structure to pass information to and from the minidriver, using minidriver provided callbacks. |
| [HW_CLOCK_OBJECT structure](..\strmini\ns-strmini--hw-clock-object.md) | The HW_CLOCK_OBJECT structure describes the clock associated with a stream. |
| [PKSSCATTER_GATHER structure](..\strmini\ns-strmini-pksscatter-gather.md) | TBD. |
| [STREAM_PROPERTY_DESCRIPTOR structure](..\strmini\ns-strmini--stream-property-descriptor.md) | STREAM_PROPERTY_DESCRIPTOR specifies the parameters of property get/set requests that the class driver passes to the minidriver. |
| [HW_STREAM_INFORMATION structure](..\strmini\ns-strmini--hw-stream-information.md) | The HW_STREAM_INFORMATION structure describes the kernel streaming semantics supported by individual streams, as part of an HW_STREAM_DESCRIPTOR structure. |
| [HW_STREAM_OBJECT structure](..\strmini\ns-strmini--hw-stream-object~r1.md) | HW_STREAM_OBJECT describes an instance of a minidriver stream. |
| [HW_STREAM_DESCRIPTOR structure](..\strmini\ns-strmini--hw-stream-descriptor.md) | The minidriver uses the HW_STREAM_DESCRIPTOR structure to return stream information to the stream class driver. |
| [STREAM_DATA_INTERSECT_INFO structure](..\strmini\ns-strmini--stream-data-intersect-info.md) | STREAM_DATA_INTERSECT_INFO describes the parameters of a data intersection operation. |
| [HW_TIME_CONTEXT structure](..\strmini\ns-strmini--hw-time-context.md) | The class driver passes an HW_TIME_CONTEXT structure as a parameter to be filled in by a stream's StrMiniClock routine, or returns a completed HW_TIME_CONTEXT structure when it responds to a StreamClassQueryMasterClock or StreamClassQueryMasterClockSync request. |
| [HW_EVENT_DESCRIPTOR structure](..\strmini\ns-strmini--hw-event-descriptor.md) | When the class driver calls one of the minidriver's StrMiniEvent routines, it passes a pointer to an HW_EVENT_DESCRIPTOR structure to describe the event as enabled or disabled. |
| [HW_INITIALIZATION_DATA structure](..\strmini\ns-strmini--hw-initialization-data.md) | The HW_INITIALIZATION_DATA structure specifies the basic information the class driver needs to begin initializing the minidriver. |
| [STREAM_METHOD_DESCRIPTOR structure](..\strmini\ns-strmini--stream-method-descriptor.md) | TBD. |
| [HW_STREAM_HEADER structure](..\strmini\ns-strmini--hw-stream-header.md) | The HW_STREAM_HEADER structure describes the kernel streaming semantics supported by the minidriver as a whole, as part of a HW_STREAM_DESCRIPTOR structure. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [KsGetBusEnumIdentifier function](..\swenum\nf-swenum-ksgetbusenumidentifier.md) | The KsGetBusEnumIdentifier function retrieves the software bus enumerator identifier for the bus device associated with the given IRP. |
| [KsServiceBusEnumPnpRequest function](..\swenum\nf-swenum-ksservicebusenumpnprequest.md) | The KsServiceBusEnumPnpRequest function services IRP_MJ_PNP requests on behalf of the demand-load bus enumerator object that was created with KsCreateBusEnumObject. |
| [KsIsBusEnumChildDevice function](..\swenum\nf-swenum-ksisbusenumchilddevice.md) | The KsIsBusEnumChildDevice function determines if the given device object is a child device of the demand-load bus enumerator object. |
| [KsCreateBusEnumObject function](..\swenum\nf-swenum-kscreatebusenumobject.md) | The KsCreateBusEnumObject function creates a demand-load bus enumerator object and initializes it for use with the demand-load bus enumerator services. |
| [KsDereferenceSoftwareBusObject function](..\swenum\nf-swenum-ksdereferencesoftwarebusobject.md) | The KsDereferenceSoftwareBusObject function decrements the reference count of the demand-load bus enumerator object's PDO. |
| [KsReferenceSoftwareBusObject function](..\swenum\nf-swenum-ksreferencesoftwarebusobject.md) | The KsReferenceSoftwareBusObject function increments the reference count of the demand-load bus enumerator object's PDO. |
| [KsRemoveBusEnumInterface function](..\swenum\nf-swenum-ksremovebusenuminterface.md) | The KsRemoveBusEnumInterface function removes an interface to the demand-load bus enumerator object. |
| [KsGetBusEnumParentFDOFromChildPDO function](..\swenum\nf-swenum-ksgetbusenumparentfdofromchildpdo.md) | The KsGetBusEnumParentFDOFromChildPDO function retrieves the FDO of the parent of the given child PDO. |
| [KsInstallBusEnumInterface function](..\swenum\nf-swenum-ksinstallbusenuminterface.md) | The KsInstallBusEnumInterface function installs an interface to the demand-load bus enumerator object. |
| [KsQuerySoftwareBusInterface function](..\swenum\nf-swenum-ksquerysoftwarebusinterface.md) | The KsQuerySoftwareBusInterface function creates a buffer from the paged pool and copies the reference string associated with the demand-load bus enumerator object's PDO into the buffer. |
| [KsGetBusEnumPnpDeviceObject function](..\swenum\nf-swenum-ksgetbusenumpnpdeviceobject.md) | The KsGetBusEnumPnpDeviceObject function retrieves the Plug and Play device object attached to the given device object. |
| [KsServiceBusEnumCreateRequest function](..\swenum\nf-swenum-ksservicebusenumcreaterequest.md) | The KsServiceBusEnumCreateRequest function services IRP_MJ_CREATE requests for the software bus device interface. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SWENUM_INSTALL_INTERFACE structure](..\swenum\ns-swenum--swenum-install-interface.md) | The SWENUM_INSTALL_INTERFACE structure describes a specific demand-load bus enumerator object interface to install. |
| [BUS_INTERFACE_SWENUM structure](..\swenum\ns-swenum--bus-interface-swenum.md) | The BUS_INTERFACE_SWENUM structure describes the demand-load bus enumerator object's interface. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_SWENUM_REMOVE_INTERFACE IOCTL](..\swenum\ni-swenum-ioctl-swenum-remove-interface.md) | The IOCTL_SWENUM_REMOVE_INTERFACE control code... |
| [IOCTL_SWENUM_INSTALL_INTERFACE IOCTL](..\swenum\ni-swenum-ioctl-swenum-install-interface.md) | The IOCTL_SWENUM_INSTALL_INTERFACE control code... |
| [IOCTL_SWENUM_GET_BUS_ID IOCTL](..\swenum\ni-swenum-ioctl-swenum-get-bus-id.md) | The IOCTL_SWENUM_GET_BUS_ID control code... |


This technology is in the following headers:


| Header        | 

| [amtvuids](..\amtvuids\~PORTAL~amtvuids.md) | 

| [avcstrm](..\avcstrm\~PORTAL~avcstrm.md) | 

| [bdasup](..\bdasup\~PORTAL~bdasup.md) | 

| [bdatypes](..\bdatypes\~PORTAL~bdatypes.md) | 

| [dsound](..\dsound\~PORTAL~dsound.md) | 

| [kcom](..\kcom\~PORTAL~kcom.md) | 

| [ks](..\ks\~PORTAL~ks.md) | 

| [ksi](..\ksi\~PORTAL~ksi.md) | 

| [ksproxy](..\ksproxy\~PORTAL~ksproxy.md) | 

| [lamp](..\lamp\~PORTAL~lamp.md) | 

| [mfapi](..\mfapi\~PORTAL~mfapi.md) | 

| [mfidl](..\mfidl\~PORTAL~mfidl.md) | 

| [msviddrv](..\msviddrv\~PORTAL~msviddrv.md) | 

| [stdunk](..\stdunk\~PORTAL~stdunk.md) | 

| [strmini](..\strmini\~PORTAL~strmini.md) | 

| [swenum](..\swenum\~PORTAL~swenum.md) | 
