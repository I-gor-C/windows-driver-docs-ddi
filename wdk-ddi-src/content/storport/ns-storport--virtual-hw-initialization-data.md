---
UID: NS.storport._VIRTUAL_HW_INITIALIZATION_DATA
title: VIRTUAL_HW_INITIALIZATION_DATA
author: windows-driver-content
description: The VIRTUAL_HW_INITIALIZATION_DATA structure contains information particular to each virtual miniport driver.
old-location: storage\virtual_hw_initialization_data.htm
old-project: storage
ms.assetid: 10e7e097-ed84-4200-b7b6-6a838a058fd2
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: VIRTUAL_HW_INITIALIZATION_DATA, VIRTUAL_HW_INITIALIZATION_DATA, *PVIRTUAL_HW_INITIALIZATION_DATA
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
req.alt-api: VIRTUAL_HW_INITIALIZATION_DATA
req.alt-loc: storport.h
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
req.iface: 
req.product: Windows 10 or later.
---

# VIRTUAL_HW_INITIALIZATION_DATA structure



## -description
<p>The <b>VIRTUAL_HW_INITIALIZATION_DATA</b> structure contains information particular to each virtual miniport driver.</p>


## -syntax

````
typedef struct _VIRTUAL_HW_INITIALIZATION_DATA {
  ULONG                       HwInitializationDataSize;
  INTERFACE_TYPE              AdapterInterfaceType;
  PHW_INITIALIZE              HwInitialize;
  PHW_STARTIO                 HwStartIo;
  PHW_INTERRUPT               HwInterrupt;
  PVIRTUAL_HW_FIND_ADAPTER    HwFindAdapter;
  PHW_RESET_BUS               HwResetBus;
  PHW_DMA_STARTED             HwDmaStarted;
  PHW_ADAPTER_STATE           HwAdapterState;
  ULONG                       DeviceExtensionSize;
  ULONG                       SpecificLuExtensionSize;
  ULONG                       SrbExtensionSize;
  ULONG                       NumberOfAccessRanges;
  PVOID                       Reserved;
  UCHAR                       MapBuffers;
  BOOLEAN                     NeedPhysicalAddresses;
  BOOLEAN                     TaggedQueuing;
  BOOLEAN                     AutoRequestSense;
  BOOLEAN                     MultipleRequestPerLu;
  BOOLEAN                     ReceiveEvent;
  USHORT                      VendorIdLength;
  PVOID                       VendorId;
  union {
    USHORT ReservedUshort;
    USHORT PortVersionFlags;
  };
  USHORT                      DeviceIdLength;
  PVOID                       DeviceId;
  PHW_ADAPTER_CONTROL         HwAdapterControl;
  PHW_BUILDIO                 HwBuildIo;
  PHW_FREE_ADAPTER_RESOURCES  HwFreeAdapterResources;
  PHW_PROCESS_SERVICE_REQUEST HwProcessServiceRequest;
  PHW_COMPLETE_SERVICE_IRP    HwCompleteServiceIrp;
  PHW_INITIALIZE_TRACING      HwInitializeTracing;
  PHW_CLEANUP_TRACING         HwCleanupTracing;
} VIRTUAL_HW_INITIALIZATION_DATA, *PVIRTUAL_HW_INITIALIZATION_DATA;
````


## -struct-fields
<dl>

### -field HwInitializationDataSize

<dd>
<p>Specifies the size of this structure in bytes, as returned by <b>sizeof</b>(). This member indicates the version of this structure that is used by the virtual miniport driver. A virtual miniport driver's <b>DriverEntry</b> routine should set this member's value for the port driver.</p>
</dd>

### -field AdapterInterfaceType

<dd>
<p>The Storport driver does not support legacy buses. Therefore, most of the adapter interface types that are used with the SCSI port driver are invalid for Storport drivers. In particular, Storport does not support Isa, Eisa, MicroChannel, and TurboChannel. Furthermore, unlike the SCSI port case, a virtual miniport driver that works with the Storport driver is not required to supply values for the <b>VendorIdLength</b>, <b>VendorId</b>, <b>DeviceIdLength</b>, and <b>DeviceId</b> members.</p>
</dd>

### -field HwInitialize

<dd>
<p>A pointer to the virtual miniport driver's <a href="storage.hwstorinitialize">HwStorInitialize</a> routine, which is a required entry point for all virtual miniport drivers.</p>
</dd>

### -field HwStartIo

<dd>
<p>A pointer to the virtual miniport driver's <a href="storage.hwstorstartio">HwStorStartIo</a> routine, which is a required entry point for all virtual miniport drivers.</p>
</dd>

### -field HwInterrupt

<dd>
<p>Not used. Virtual miniport drivers do not process interrupts.</p>
</dd>

### -field HwFindAdapter

<dd>
<p>A pointer to the virtual miniport driver's <a href="storage.virtualhwstorfindadapter">VirtualHwStorFindAdapter</a> routine, which is a required entry point for all virtual miniport drivers.</p>
</dd>

### -field HwResetBus

<dd>
<p>A pointer to the virtual miniport driver's <a href="storage.hwstorresetbus">HwStorResetBus</a> routine, which is a required entry point for all virtual miniport drivers.</p>
</dd>

### -field HwDmaStarted

<dd>
<p>Not used. Virtual miniport drivers do not perform DMA.</p>
</dd>

### -field HwAdapterState

<dd>
<p>The Storport driver does not support legacy drivers. Therefore, this member must be <b>NULL</b>.</p>
</dd>

### -field DeviceExtensionSize

<dd>
<p>Specifies the size, in bytes, that is required by the virtual miniport driver for its per-adapter non-paged device extension. A virtual miniport driver uses its device extension as storage for driver-determined adapter information. The operating system-specific port driver initializes each device extension that it allocates with zeros, and passes a pointer to the adapter-specific device extension in most calls to the virtual miniport driver. The given size does not include any virtual miniport driver-requested per-logical-unit storage.</p>
</dd>

### -field SpecificLuExtensionSize

<dd>
<p>Specifies the size, in bytes, that is required by the virtual miniport driver for its per-logical-unit non-paged storage, if any. A virtual miniport driver can use its logical unit (LU) extensions as storage for driver-determined LU information about peripherals on the virtual bus. The operating system-specific port driver initializes each LU extension that it allocates with zeros. Leave this member set to zero if the virtual miniport driver does not maintain per-LU information for which it requires storage.</p>
</dd>

### -field SrbExtensionSize

<dd>
<p>Specifies the size, in bytes, that is required by the virtual miniport driver for its per-request non-paged storage, if any. Because virtual miniport drivers that work with the Storport driver must support scatter/gather lists, and the per-SRB scatter/gather lists are usually allocated in the SRB extension, this member is rarely zero.</p>
</dd>

### -field NumberOfAccessRanges

<dd>
<p>Not used. Virtual miniport drivers do not support hardware.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for system use.</p>
</dd>

### -field MapBuffers

<dd>
<p>Not valid for virtual miniport drivers. The virtual miniport driver must map all data buffers into virtual address space.</p>
</dd>

### -field NeedPhysicalAddresses

<dd>
<p>Not used. Virtual miniport drivers do not support hardware.</p>
</dd>

### -field TaggedQueuing

<dd>
<p>Must be set to <b>TRUE</b>. A value of <b>TRUE</b> indicates that the virtual miniport driver supports tagged queuing.</p>
</dd>

### -field AutoRequestSense

<dd>
<p>Must be set to <b>TRUE</b>. A value of <b>TRUE</b> indicates that the HBA can perform a request-sense operation without requiring an explicit request to do so.</p>
</dd>

### -field MultipleRequestPerLu

<dd>
<p>Must be set to <b>TRUE</b>. A value of <b>TRUE</b> indicates that the virtual miniport driver can queue multiple requests per logical unit (LU).</p>
</dd>

### -field ReceiveEvent

<dd>
<p>Must be set to <b>TRUE</b>. A value of <b>TRUE</b> indicates that the virtual miniport driver supports receive events.</p>
</dd>

### -field VendorIdLength

<dd>
<p>The length, in bytes, of the vendor identifier.</p>
</dd>

### -field VendorId

<dd>
<p>The vendor identifier.</p>
</dd>

### -field ReservedUshort

<dd>
<p>Reserved.</p>
</dd>

### -field PortVersionFlags

<dd>
<p>A bitmap of flags that indicate the features that the port driver supports. Currently, the only flag available is SP_VER_TRACE_SUPPORT, which indicates that the port driver supports tracing.</p>
</dd>

### -field DeviceIdLength

<dd>
<p>The length, in bytes, of the device identifier.</p>
</dd>

### -field DeviceId

<dd>
<p>The device identifier.</p>
</dd>

### -field HwAdapterControl

<dd>
<p>A pointer to the virtual miniport driver's <a href="storage.hwstoradaptercontrol">HwStorAdapterControl</a> routine. </p>
</dd>

### -field HwBuildIo

<dd>
<p>
      This member is not used.</p>
</dd>

### -field HwFreeAdapterResources

<dd>
<p>A pointer to the virtual miniport driver's <a href="storage.hwstorfreeadapterresources">HwStorFreeAdapterResources</a> routine, which is a required entry point for all virtual miniport drivers.</p>
</dd>

### -field HwProcessServiceRequest

<dd>
<p>A pointer to the virtual miniport driver's <a href="storage.hwstorprocessservicerequest">HwStorProcessServiceRequest</a> routine.</p>
</dd>

### -field HwCompleteServiceIrp

<dd>
<p>A pointer to the virtual miniport driver's <a href="storage.hwstorcompleteserviceirp">HwStorCompleteServiceIrp</a> routine.</p>
</dd>

### -field HwInitializeTracing

<dd>
<p>A pointer to the virtual miniport driver's <a href="storage.hwstorinitializetracing">HwStorInitializeTracing</a> routine.</p>
</dd>

### -field HwCleanupTracing

<dd>
<p>A pointer to the virtual miniport driver's <a href="storage.hwstorcleanuptracing">HwStorCleanupTracing</a> routine.</p>
</dd>
</dl>

## -remarks
<p>If a virtual miniport driver will execute only on Windows 8 or later, the driver should use the <a href="storage.hw_initialization_data__storport_">HW_INITIALIZATION_DATA</a> structure instead of <b>VIRTUAL_HW_INITIALIZATION_DATA</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.hwstoradaptercontrol">HwStorAdapterControl</a>
</dt>
<dt>
<a href="storage.hwstorcleanuptracing">HwStorCleanupTracing</a>
</dt>
<dt>
<a href="storage.hwstorcompleteserviceirp">HwStorCompleteServiceIrp</a>
</dt>
<dt>
<a href="storage.hwstorfreeadapterresources">HwStorFreeAdapterResources</a>
</dt>
<dt>
<a href="storage.hwstorinitialize">HwStorInitialize</a>
</dt>
<dt>
<a href="storage.hwstorinitializetracing">HwStorInitializeTracing</a>
</dt>
<dt>
<a href="storage.hwstorprocessservicerequest">HwStorProcessServiceRequest</a>
</dt>
<dt>
<a href="storage.hwstorresetbus">HwStorResetBus</a>
</dt>
<dt>
<a href="storage.hwstorstartio">HwStorStartIo</a>
</dt>
<dt>
<a href="storage.virtualhwstorfindadapter">VirtualHwStorFindAdapter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20VIRTUAL_HW_INITIALIZATION_DATA structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
