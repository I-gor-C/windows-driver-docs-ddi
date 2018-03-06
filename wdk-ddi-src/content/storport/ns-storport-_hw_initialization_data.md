---
UID: NS:storport._HW_INITIALIZATION_DATA
title: "_HW_INITIALIZATION_DATA"
author: windows-driver-content
description: The HW_INITIALIZATION_DATA (Storport) structure contains information particular to each miniport driver and the hardware that the miniport driver manages.
old-location: storage\hw_initialization_data__storport_.htm
old-project: storage
ms.assetid: 54f460da-2dfb-4a9d-9b25-edb90f3bfdd5
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PHW_INITIALIZATION_DATA, ADDRESS_TYPE_FLAG_BTL8, HW_INITIALIZATION_DATA, HW_INITIALIZATION_DATA structure [Storage Devices], PHW_INITIALIZATION_DATA, PHW_INITIALIZATION_DATA structure pointer [Storage Devices], SRB_TYPE_FLAG_SCSI_REQUEST_BLOCK, SRB_TYPE_FLAG_STORAGE_REQUEST_BLOCK, STOR_FEATURE_ATA_PASS_THROUGH, STOR_FEATURE_DEVICE_DESCRIPTOR_FROM_ATA_INFO_VPD, STOR_FEATURE_DEVICE_NAME_NO_SUFFIX, STOR_FEATURE_DUMP_POINTERS, STOR_FEATURE_DUMP_RESUME_CAPABLE, STOR_FEATURE_FULL_PNP_DEVICE_CAPABILITIES, STOR_FEATURE_SET_ADAPTER_INTERFACE_TYPE, STOR_FEATURE_VIRTUAL_MINIPORT, STOR_MAP_ALL_BUFFERS, STOR_MAP_ALL_BUFFERS_INCLUDING_READ_WRITE, STOR_MAP_NON_READ_WRITE_BUFFERS, STOR_MAP_NO_BUFFERS, _HW_INITIALIZATION_DATA, _HW_INITIALIZATION_DATA structure [Storage Devices], storage.hw_initialization_data__storport_, storport/HW_INITIALIZATION_DATA, storport/PHW_INITIALIZATION_DATA, structs-storport_c3d0ed59-9662-409d-acc3-6c2358837a01.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Storport.h
api_name:
-	HW_INITIALIZATION_DATA
product: Windows
targetos: Windows
req.typenames: HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA, HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA
req.product: Windows 10 or later.
---

# _HW_INITIALIZATION_DATA structure
The <b>HW_INITIALIZATION_DATA (Storport)</b> structure contains information particular to each miniport driver and the hardware that the miniport driver manages.

## Syntax
````
typedef struct _HW_INITIALIZATION_DATA {
  ULONG                       HwInitializationDataSize;
  INTERFACE_TYPE              AdapterInterfaceType;
  PHW_INITIALIZE              HwInitialize;
  PHW_STARTIO                 HwStartIo;
  PHW_INTERRUPT               HwInterrupt;
  PHW_FIND_ADAPTER            HwFindAdapter;
  PHW_RESET_BUS               HwResetBus;
  PHW_DMA_STARTED             HwDmaStarted;
  PHW_ADAPTER_STATE           HwAdapterState;
  ULONG                       DeviceExtensionSize;
  ULONG                       SpecificLuExtensionSize;
  ULONG                       SrbExtensionSize;
  ULONG                       NumberOfAccessRanges;
  PVOID                       Reserved;
  BOOLEAN                     MapBuffers;
  BOOLEAN                     NeedPhysicalAddresses;
  BOOLEAN                     TaggedQueuing;
  BOOLEAN                     AutoRequestSense;
  BOOLEAN                     MultipleRequestPerLu;
  BOOLEAN                     ReceiveEvent;
  USHORT                      VendorIdLength;
  PVOID                       VendorId;
  USHORT                      PortVersionFlags;
  USHORT                      DeviceIdLength;
  PVOID                       DeviceId;
  PHW_STOP_ADAPTER            HwAdapterControl;
  PHW_BUILDIO                 HwBuildIo;
#if (NTDDI_VERSION >= NTDDI_WIN8)
  PHW_FREE_ADAPTER_RESOURCES  HwFreeAdapterResources;
  PHW_PROCESS_SERVICE_REQUEST HwProcessServiceRequest;
  PHW_COMPLETE_SERVICE_IRP    HwCompleteServiceIrp;
  PHW_INITIALIZE_TRACING      HwInitializeTracing;
  PHW_CLEANUP_TRACING         HwCleanupTracing;
  PHW_TRACING_ENABLED         HwTracingEnabled;
  ULONG                       FeatureSupport;
  ULONG                       SrbTypeFlags;
  ULONG                       AddressTypeFlags;
  ULONG                       Reserved1;
  PHW_UNIT_CONTROL            HwUnitControl;
#endif 
} HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA;
````

## Members


`AdapterInterfaceType`

The Storport driver does not support legacy buses. Therefore, most of the adapter interface types used with the SCSI Port driver are invalid for Storport. In particular, <b>Isa</b>, <b>Eisa</b>, <b>MicroChannel</b>, and <b>TurboChannel</b> are not supported. Furthermore, unlike the SCSI Port case, a miniport driver that works with the Storport driver is not required to supply values for the <b>VendorIdLength</b>, <b>VendorId</b>, <b>DeviceIdLength</b>, and <b>DeviceId</b> members.

`AutoRequestSense`

Must be <b>TRUE</b>. A value of <b>TRUE</b> indicates that the HBA can perform a request-sense operation without requiring an explicit request to do so. All miniport drivers that work with the Storport driver must support SCSI Auto-Request Sense.

`DeviceExtensionSize`

Specifies the size, in bytes, required by the miniport driver for its per-adapter device extension. A miniport driver uses its device extension as storage for driver-determined host bus adapter (HBA) information. The operating system-specific port driver initializes each device extension one time, when it first allocates the extension and fills it with zeros. It passes a pointer to the HBA-specific device extension in every call to a miniport driver. The given size does not include any miniport driver-requested per-logical-unit storage. The size of per-logical-unit storage is specified via the <b>SpecificLuExtensionSize</b> field, described later in this topic.

Although SCSIPort re-initializes the device extension whenever the adapter is stopped and thus subsequent calls to <a href="..\srb\nc-srb-phw_find_adapter.md">HwScsiFindAdapter</a> receive a zeroed-out device extension, Storport does not follow that model. Rather, Storport resets the device extension to zero only when it is first allocated, so only the first call to <a href="..\storport\nc-storport-hw_find_adapter.md">HwStorFindAdapter</a> for a given adapter receives a zeroed-out device extension. Subsequent calls to <b>HwStorFindAdapter</b> and other miniport functions receive the device extension as last modified by the miniport. This allows the miniport driver to maintain knowledge about the state of the adapter between Plug and Play (PnP) stops and restarts, possibly enabling the miniport driver to optimize it's initialization procedure.

`DeviceId`

The Storport driver ignores this member, because miniport drivers that work with the Storport driver must support PnP.

`DeviceIdLength`

The Storport driver ignores this member, because miniport drivers that work with the Storport driver must support PnP.

`HwAdapterControl`

Pointer to the miniport driver's <a href="..\storport\nc-storport-hw_adapter_control.md">HwStorAdapterControl</a> routine. This is a required routine because miniport drivers that work with the Storport driver require PnP support.

`HwAdapterState`

The Storport driver does not support legacy drivers. Therefore, this member must be <b>NULL</b>.

`HwBuildIo`

Pointer to an optional <a href="..\storport\nc-storport-hw_buildio.md">HwStorBuildIo</a> routine that the port driver calls to do unsynchronized processing prior to calling the miniport driver's <a href="..\storport\nc-storport-hw_startio.md">HwStorStartIo</a> routine.

`HwDmaStarted`

The Storport driver does not support subordinate-mode DMA. Therefore, this member must be <b>NULL</b>.

`HwFindAdapter`

Pointer to the miniport driver's <a href="..\storport\nc-storport-hw_find_adapter.md">HwStorFindAdapter</a> routine, which is a required entry point for all miniport drivers.

`HwInitializationDataSize`

Specifies the size of this structure in bytes, as returned by <b>sizeof</b>(HW_INITIALIZATION_DATA). In effect, this member indicates the version of this structure being used by the miniport driver. A miniport driver's DriverEntry routine should set this member's value for the port driver.

`HwInitialize`

Pointer to the miniport driver's <a href="..\storport\nc-storport-hw_initialize.md">HwStorInitialize</a> routine, which is a required entry point for all miniport drivers.

`HwInterrupt`

Pointer to the miniport driver's <a href="..\storport\nc-storport-hw_interrupt.md">HwStorInterrupt</a> routine, which is a required entry point for all miniport drivers.

`HwResetBus`

Pointer to the miniport driver's <a href="..\storport\nc-storport-hw_reset_bus.md">HwStorResetBus</a> routine, which is a required entry point for all miniport drivers.

`HwStartIo`

Pointer to the miniport driver's <a href="..\storport\nc-storport-hw_startio.md">HwStorStartIo</a> routine, which is a required entry point for all miniport drivers.

`MapBuffers`

Indicates whether the Storport driver maps SRB data buffer addresses to system virtual addresses. The <b>MapBuffers</b> member can have one of the following values.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="STOR_MAP_NO_BUFFERS"></a><a id="stor_map_no_buffers"></a><dl>
<dt><b>STOR_MAP_NO_BUFFERS</b></dt>
</dl>
</td>
<td width="60%">
Do not map for any SRB except SRB_FUNCTION_IO_CONTROL and SRB_FUNCTION_WMI.

</td>
</tr>
<tr>
<td width="40%"><a id="STOR_MAP_ALL_BUFFERS"></a><a id="stor_map_all_buffers"></a><dl>
<dt><b>STOR_MAP_ALL_BUFFERS</b></dt>
</dl>
</td>
<td width="60%">
Obsolete. This value has the same effect as STOR_MAP_NON_READ_WRITE_BUFFERS.

</td>
</tr>
<tr>
<td width="40%"><a id="STOR_MAP_NON_READ_WRITE_BUFFERS"></a><a id="stor_map_non_read_write_buffers"></a><dl>
<dt><b>STOR_MAP_NON_READ_WRITE_BUFFERS</b></dt>
</dl>
</td>
<td width="60%">
Map the buffer for all I/O except for read or write requests.

</td>
</tr>
<tr>
<td width="40%"><a id="STOR_MAP_ALL_BUFFERS_INCLUDING_READ_WRITE"></a><a id="stor_map_all_buffers_including_read_write"></a><dl>
<dt><b>STOR_MAP_ALL_BUFFERS_INCLUDING_READ_WRITE</b></dt>
</dl>
</td>
<td width="60%">
Map the buffer for all I/O including read and write requests. This value is valid starting with Windows 8.

</td>
</tr>
</table>

`MultipleRequestPerLu`

Must be set to <b>TRUE</b>. A value of <b>TRUE</b> indicates that the miniport driver can queue multiple requests per logical unit. Miniport drivers that work with the Storport driver must support multiple requests per logical unit.

`NeedPhysicalAddresses`

Must be set to <b>TRUE</b>. A value of <b>TRUE</b> indicates that the miniport driver must translate certain types of addresses to physical addresses. Miniport drivers that work with the Storport driver must support bus-master DMA, so they will always be required to do address translation.

`NumberOfAccessRanges`

Specifies how many access ranges the adapter uses. Each is a range either of memory addresses or I/O port addresses.

`ReceiveEvent`

The Storport driver ignores this member.

`Reserved`

Reserved for system use and not available for use by miniport drivers.

`SpecificLuExtensionSize`

Specifies the size in bytes required by the miniport driver for its per-logical-unit storage, if any. A miniport driver can use its LU extensions as storage for driver-determined logical-unit information about  peripherals on the bus. The Storport driver initializes each LU extension it allocates with zeros. Leave this member set to zero if the miniport driver does not maintain per-LU information for which it requires storage. This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as <a href="..\storport\nf-storport-storportgetuncachedextension.md">StorPortGetUncachedExtension</a>.

`SrbExtensionSize`

Specifies the size, in bytes, required by the miniport driver for its per-request storage, if any. A miniport driver can use SRB extensions as storage for driver-determined, request-specific information, such as data necessary to process a particular request. The Storport driver does not initialize SRB extensions, but sets a pointer to this storage in each SRB it sends to the miniport driver. An SRB extension can be safely accessed by the HBA hardware. Because miniport drivers that work with the Storport driver must support scatter/gather lists, and the per-SRB scatter/gather lists are usually allocated in the SRB extension, this member is rarely zero. Leave this member set to zero if the miniport driver does not maintain per-SRB information for which it requires storage. 

This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as <a href="..\storport\nf-storport-storportgetuncachedextension.md">StorPortGetUncachedExtension.</a>.

`TaggedQueuing`

Must be set to <b>TRUE</b>. A value of <b>TRUE</b> indicates that the miniport driver supports SCSI tagged queuing. All miniport drivers that work with the Storport driver must support tagged queuing.

`VendorId`

The Storport driver ignores this member, because miniport drivers that work with the Storport driver must support PnP.

`VendorIdLength`

The Storport driver ignores this member, because miniport drivers that work with the Storport driver must support PnP.

## Remarks
The Storport driver follows the SCSI port driver's PnP initialization model. During the driver's DriverEntry routine, the miniport driver calls the <a href="..\storport\nf-storport-storportinitialize.md">StorPortInitialize</a> routine with a <b>HW_INITIALIZATION_DATA</b> structure describing the hardware it supports. Later, when the PnP Manager sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a> request to the port driver, the port driver passes a <a href="..\strmini\ns-strmini-_port_configuration_information.md">PORT_CONFIGURATION_INFORMATION</a> structure to the miniport driver's <a href="..\storport\nc-storport-hw_find_adapter.md">HwStorFindAdapter</a> routine. Afterwards, the port driver calls <a href="..\storport\nc-storport-hw_initialize.md">HwStorInitialize</a> to initialize the adapter.

Starting in Windows 8, both physical and virtual Storport miniports use <b>HW_INITIALIZATION_DATA</b>. See <a href="..\storport\ns-storport-_virtual_hw_initialization_data.md">VIRTUAL_HW_INITIALIZATION_DATA</a> for more on which members are required for virtual miniports.

 If a miniport driver sets the flag, <b>STOR_FEATURE_SET_ADAPTER_INTERFACE_TYPE</b> in <b>HW_INITIALIZATION_DATA</b>, it should also set <b>AdapterInterfaceType</b> to <b>InterfaceTypeUndefined</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | storport.h (include Storport.h) |

## See Also

<a href="..\storport\nc-storport-hw_reset_bus.md">HwStorResetBus</a>



<a href="..\storport\nc-storport-hw_buildio.md">HwStorBuildIo</a>



<a href="..\storport\nc-storport-hw_interrupt.md">HwStorInterrupt</a>



<a href="..\storport\nc-storport-hw_startio.md">HwStorStartIo</a>



<a href="..\storport\nc-storport-hw_find_adapter.md">HwStorFindAdapter</a>



<a href="..\storport\nf-storport-storportinitialize.md">StorPortInitialize</a>



<a href="..\storport\ns-storport-_virtual_hw_initialization_data.md">VIRTUAL_HW_INITIALIZATION_DATA</a>



<a href="..\storport\nc-storport-hw_adapter_control.md">HwStorAdapterControl</a>



<a href="..\storport\nc-storport-hw_initialize.md">HwStorInitialize</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20_HW_INITIALIZATION_DATA structure%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>