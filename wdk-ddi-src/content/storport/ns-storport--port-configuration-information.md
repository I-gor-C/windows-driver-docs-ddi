---
UID: NS.storport._PORT_CONFIGURATION_INFORMATION
title: PORT_CONFIGURATION_INFORMATION
author: windows-driver-content
description: The PORT_CONFIGURATION_INFORMATION contains configuration information for a host bus adapter (HBA).
old-location: storage\port_configuration_information__storport_.htm
old-project: storage
ms.assetid: ef710755-4437-4b17-b0ab-259a94d87545
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PORT_CONFIGURATION_INFORMATION, PORT_CONFIGURATION_INFORMATION, *PPORT_CONFIGURATION_INFORMATION
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
req.alt-api: PORT_CONFIGURATION_INFORMATION
req.alt-loc: Storport.h
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

# PORT_CONFIGURATION_INFORMATION structure



## -description
<p>The <b>PORT_CONFIGURATION_INFORMATION</b> contains configuration information for a host bus adapter (HBA). </p>


## -syntax

````
typedef struct _PORT_CONFIGURATION_INFORMATION {
  ULONG                                  Length;
  ULONG                                  SystemIoBusNumber;
  INTERFACE_TYPE                         AdapterInterfaceType;
  ULONG                                  BusInterruptLevel;
  ULONG                                  BusInterruptVector;
  KINTERRUPT_MODE                        InterruptMode;
  ULONG                                  MaximumTransferLength;
  ULONG                                  NumberOfPhysicalBreaks;
  ULONG                                  DmaChannel;
  ULONG                                  DmaPort;
  DMA_WIDTH                              DmaWidth;
  DMA_SPEED                              DmaSpeed;
  ULONG                                  AlignmentMask;
  ULONG                                  NumberOfAccessRanges;
  ACCESS_RANGE                           (*AccessRanges)[];
#if (NTDDI_VERSION >= NTDDI_WIN8)
  PVOID                                  MiniportDumpData;
#else 
  PVOID                                  Reserved;
#endif 
  UCHAR                                  NumberOfBuses;
  UCHAR                                  InitiatorBusId[8];
  BOOLEAN                                ScatterGather;
  BOOLEAN                                Master;
  BOOLEAN                                CachesData;
  BOOLEAN                                AdapterScansDown;
  BOOLEAN                                AtdiskPrimaryClaimed;
  BOOLEAN                                AtdiskSecondaryClaimed;
  BOOLEAN                                Dma32BitAddresses;
  BOOLEAN                                DemandMode;
  UCHAR                                  MapBuffers;
  BOOLEAN                                NeedPhysicalAddresses;
  BOOLEAN                                TaggedQueuing;
  BOOLEAN                                AutoRequestSense;
  BOOLEAN                                MultipleRequestPerLu;
  BOOLEAN                                ReceiveEvent;
  BOOLEAN                                RealModeInitialized;
  BOOLEAN                                BufferAccessScsiPortControlled;
  UCHAR                                  MaximumNumberOfTargets;
#if (NTDDI_VERSION >= NTDDI_WIN8)
  UCHAR                                  SrbType;
  UCHAR                                  AddressType;
#else 
  UCHAR                                  ReservedUchars[2];
#endif 
  ULONG                                  SlotNumber;
  ULONG                                  BusInterruptLevel2;
  ULONG                                  BusInterruptVector2;
  KINTERRUPT_MODE                        InterruptMode2;
  ULONG                                  DmaChannel2;
  ULONG                                  DmaPort2;
  DMA_WIDTH                              DmaWidth2;
  DMA_SPEED                              DmaSpeed2;
  ULONG                                  DeviceExtensionSize;
  ULONG                                  SpecificLuExtensionSize;
  ULONG                                  SrbExtensionSize;
  UCHAR                                  Dma64BitAddresses;
  BOOLEAN                                ResetTargetSupported;
  UCHAR                                  MaximumNumberOfLogicalUnits;
  BOOLEAN                                WmiDataProvider;
  STOR_SYNCHRONIZATION_MODEL             SynchronizationModel;
  PHW_MESSAGE_SIGNALED_INTERRUPT_ROUTINE HwMSInterruptRoutine;
  INTERRUPT_SYNCHRONIZATION_MODE         InterruptSynchronizationMode;
  MEMORY_REGION                          DumpRegion;
  ULONG                                  RequestedDumpBufferSize;
  BOOLEAN                                VirtualDevice;
#if (NTDDI_VERSION >= NTDDI_WIN8)
  UCHAR                                  DumpMode;
#endif 
  ULONG                                  ExtendedFlags1;
  ULONG                                  MaxNumberOfIO;
#if (NTDDI_VERSION >= NTDDI_WIN8)
  ULONG                                  MaxIOsPerLun;
  ULONG                                  InitialLunQueueDepth;
  ULONG                                  BusResetHoldTime;
  ULONG                                  FeatureSupport;
#endif 
} PORT_CONFIGURATION_INFORMATION, *PPORT_CONFIGURATION_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>Specifies the size of the <b>PORT_CONFIGURATION_INFORMATION</b> structure, in bytes. Initialized by the Storport driver, this member also serves as the structure version.</p>
</dd>

### -field <b>SystemIoBusNumber</b>

<dd>
<p>Specifies the system-assigned number of the I/O bus to which the HBA is connected. Miniport drivers must not modify this member. This Storport driver assigns this value because the platform might have several I/O buses of the specified <b>AdapterInterfaceType</b>.</p>
</dd>

### -field <b>AdapterInterfaceType</b>

<dd>
<p>Identifies the I/O bus interface. The Storport driver initializes this member to the value specified by the miniport driver in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a>  structure. Miniport drivers must not modify this member.  </p>
</dd>

### -field <b>BusInterruptLevel</b>

<dd>
<p>Specifies the bus-relative interrupt request level. The Storport port driver makes no assumptions about the HBA's interrupt usage, so the default value is zero. The Storport driver initializes this member and miniport drivers must not modify it.</p>
</dd>

### -field <b>BusInterruptVector</b>

<dd>
<p>Specifies the bus-relative vector returned by the HBA. The Storport driver makes no assumptions about the HBA's interrupt usage, so the default value is zero. This member is irrelevant to drivers that set up the <b>BusInterruptLevel</b> member for their HBAs. It is pertinent for HBAs on types of I/O buses that use interrupt vectors, such as <b>PCIBus</b>. The Storport driver initializes this member and miniport drivers must not modify it.</p>
</dd>

### -field <b>InterruptMode</b>

<dd>
<p>Specifies whether the HBA uses <b>LevelSensitive</b> or <b>Latched</b> (sometimes called "edge-triggered") interrupts. The Storport driver initializes this member to an appropriate value for the bus and the device—for example, <b>LevelSensitive</b> for <b>PCIBus</b>. The Storport driver initializes this member and miniport drivers must not modify it.</p>
</dd>

### -field <b>MaximumTransferLength</b>

<dd>
<p>Specifies the maximum number of bytes the HBA can transfer in a single transfer operation. By default, the value of this member is SP_UNINITIALIZED_VALUE, which indicates an unlimited maximum transfer size. If its HBA has more limited transfer support, a miniport driver must reset this member according to the HBA's transfer capacity. If a miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff557403">HwStorInterrupt</a> routine cannot disable interrupts on the HBA, this member can be adjusted during driver development to ensure that time spent in that miniport driver's ISR does not degrade overall system performance.</p>
</dd>

### -field <b>NumberOfPhysicalBreaks</b>

<dd>
<p>Specifies the maximum number of physical pages the storage adapter can manage in a single transfer (in other words, the extent of its scatter/gather support). By default, the value of this member is 0x11. The miniport driver must reset this member according to the storage adapter's capability.</p>
</dd>

### -field <b>DmaChannel</b>

<dd>
<p>Specifies the DMA channel used by a subordinate HBA. By default, the value of this member is SP_UNINITIALIZED_VALUE. The Storport driver initializes this member and miniport drivers must not modify it.</p>
</dd>

### -field <b>DmaPort</b>

<dd>
<p>Specifies the DMA port used by a subordinate HBA. By default, the value of this member is SP_UNINITIALIZED_VALUE. The Storport driver initializes this member and miniport drivers must not modify it.</p>
</dd>

### -field <b>DmaWidth</b>

<dd>
<p>Specifies the width of DMA transfers if the HBA uses DMA. By default, the value of this member is zero. The Storport driver initializes this member and miniport drivers must not modify it.</p>
</dd>

### -field <b>DmaSpeed</b>

<dd>
<p>Specifies the DMA data-transfer speed for <b>Eisa</b> HBAs. The Storport driver initializes this member and miniport drivers must not modify it.</p>
</dd>

### -field <b>AlignmentMask</b>

<dd>
<p>Contains a mask indicating the alignment restrictions for buffers required by the HBA for transfer operations. Some example valid mask values are 0 (byte aligned), 1 (word aligned), 3 (DWORD aligned) and 7 (double DWORD aligned). The miniport driver should set this mask if the HBA supports scatter/gather. </p>
<p>
<p>The following allowed alignment mask values are defined in <i>wdm.h</i>.</p>
</p>
<dl>

### -field <a id="FILE_BYTE_ALIGNMENT"></a><a id="file_byte_alignment"></a><b>FILE_BYTE_ALIGNMENT</b> (0x00000000)


### -field <a id="FILE_WORD_ALIGNMENT"></a><a id="file_word_alignment"></a><b>FILE_WORD_ALIGNMENT</b> (0x00000001)


### -field <a id="FILE_LONG_ALIGNMENT"></a><a id="file_long_alignment"></a><b>FILE_LONG_ALIGNMENT</b> (0x00000003)


### -field <a id="FILE_QUAD_ALIGNMENT"></a><a id="file_quad_alignment"></a><b>FILE_QUAD_ALIGNMENT</b> (0x00000007)


### -field <a id="FILE_OCTA_ALIGNMENT"></a><a id="file_octa_alignment"></a><b>FILE_OCTA_ALIGNMENT</b> (0x0000000f)


### -field <a id="FILE_32_BYTE_ALIGNMENT"></a><a id="file_32_byte_alignment"></a><b>FILE_32_BYTE_ALIGNMENT</b> (0x0000001f)


### -field <a id="FILE_64_BYTE_ALIGNMENT"></a><a id="file_64_byte_alignment"></a><b>FILE_64_BYTE_ALIGNMENT</b> (0x0000003f)


### -field <a id="FILE_128_BYTE_ALIGNMENT"></a><a id="file_128_byte_alignment"></a><b>FILE_128_BYTE_ALIGNMENT</b> (0x0000007f)


### -field <a id="FILE_256_BYTE_ALIGNMENT"></a><a id="file_256_byte_alignment"></a><b>FILE_256_BYTE_ALIGNMENT</b> (0x000000ff)


### -field <a id="FILE_512_BYTE_ALIGNMENT"></a><a id="file_512_byte_alignment"></a><b>FILE_512_BYTE_ALIGNMENT</b> (0x000001ff)

</dl>
</dd>

### -field <b>NumberOfAccessRanges</b>

<dd>
<p>Specifies the number of <b>AccessRanges</b> elements in the array, described next. </p>
</dd>

### -field <b>(*AccessRanges)</b>

<dd>
<p>Pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff550117">ACCESS_RANGE</a>-type elements. The Storport driver allocates memory for the access ranges and initializes this member. Mniport drivers must not modify this member.</p>
</dd>

### -field <b>MiniportDumpData</b>

<dd>
<p>Pointer to a dump context used during a crashdump or a hibernation.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>NumberOfBuses</b>

<dd>
<p>Specifies the number of buses controlled by the adapter. By default, the value of this member is zero. This member has a maximum value of SCSI_MAXIMUM_BUSES_PER_ADAPTER. </p>
</dd>

### -field <b>InitiatorBusId</b>

<dd>
<p>Indicates the initiator bus ID. If the input <b>InitiatorBusId</b>[0] has the value SP_UNINITIALIZED_VALUE, the miniport driver can assign a default value if its HBA does not require the use of particular value(s) determined by querying the HBA. Otherwise, the miniport driver should use any nonzero value assigned by the port driver if possible. Typically, this value is bounded by the value set for <b>MaximumNumberOfTargets</b>. </p>
</dd>

### -field <b>ScatterGather</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the HBA supports scatter/gather. The Storport driver initializes this member to <b>TRUE</b>, because its miniport drivers must support scatter/gather. Miniport drivers that work with the Storport driver must <i>not</i> modify this value.</p>
<p>Starting in Windows Server 2008 R2 and Windows 7, the Storport driver initializes this member to <b>TRUE</b>. In prior versions of Windows, however, the value is set to <b>FALSE</b>. In this case, miniport drivers must set this member to <b>TRUE</b>. Otherwise, not setting this member to <b>TRUE</b> will cause the HBA device to fail to start.</p>
</dd>

### -field <b>Master</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the HBA is a bus master. The Storport driver initializes this member to <b>TRUE</b>, because its miniport drivers must support bus-mastering DMA. Miniport drivers that work with the Storport driver must <i>not</i> modify this value. </p>
<p>Starting in Windows Server 2008 R2 and Windows 7, the Storport driver initializes this member to <b>TRUE</b>. In prior versions of Windows, however, the value is set to <b>FALSE</b>. In this case, miniport drivers must set this member to <b>TRUE</b>. Otherwise, not setting this member to <b>TRUE</b> will cause the HBA device to fail to start.</p>
</dd>

### -field <b>CachesData</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the HBA caches data or maintains cached state on the peripherals. When <b>FALSE</b> the HBA does not cache data or maintain cached state on the peripherals. By default, the value of this member is <b>FALSE</b>. If this is reset to <b>TRUE</b>, the Storport port driver notifies the miniport driver when certain system events occur, such as file system cache flushes. </p>
</dd>

### -field <b>AdapterScansDown</b>

<dd>
<p>The Storport driver ignores this member. </p>
</dd>

### -field <b>AtdiskPrimaryClaimed</b>

<dd>
<p>The Storport driver does not use this member, and its miniport drivers must not set it. </p>
</dd>

### -field <b>AtdiskSecondaryClaimed</b>

<dd>
<p>The Storport driver does not use this member, and its miniport drivers must not set it. </p>
</dd>

### -field <b>Dma32BitAddresses</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the HBA has 32 address lines and can access memory with physical addresses greater than 0x00FFFFFF. The Storport driver initializes this member to <b>TRUE</b>, because its miniport drivers must support bus-width DMA. Miniport drivers must not modify this value since this the default DMA addressing if a value for <b>Dma64BitAddresses</b> is not set. </p>
<div class="alert"><b>Note</b>  If only 32 bit addresses are supported by the device hardware, then <b>Dma64BitAddresses</b> must be set to 0.</div>
<div> </div>
</dd>

### -field <b>DemandMode</b>

<dd>
<p>Indicates the system DMA controller should be programmed for demand-mode rather than single-cycle operations. The Storport driver initializes this member to <b>FALSE</b>, because it does not support subordinate-mode DMA. Miniport drivers must not modify this value.</p>
</dd>

### -field <b>MapBuffers</b>

<dd>
<p>Indicates whether the Storport driver maps SRB data buffer addresses to system virtual addresses. The miniport driver sets this member to one of the following values to control mapping for SRB data buffer addresses.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="STOR_MAP_NO_BUFFERS"></a><a id="stor_map_no_buffers"></a><dl>

### -field <b>STOR_MAP_NO_BUFFERS</b>

</dl>
</td>
<td width="60%">
<p>Maps the buffer only for SRB_FUNCTION_IO_CONTROL and SRB_FUNCTION_WMI.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STOR_MAP_ALL_BUFFERS"></a><a id="stor_map_all_buffers"></a><dl>

### -field <b>STOR_MAP_ALL_BUFFERS</b>

</dl>
</td>
<td width="60%">
<p>Obsolete. This value has the same effect as STOR_MAP_NON_READ_WRITE_BUFFERS.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STOR_MAP_NON_READ_WRITE_BUFFERS"></a><a id="stor_map_non_read_write_buffers"></a><dl>

### -field <b>STOR_MAP_NON_READ_WRITE_BUFFERS</b>

</dl>
</td>
<td width="60%">
<p>Maps the buffer all for IO except for read and write requests.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STOR_MAP_ALL_BUFFERS_INCLUDING_READ_WRITE"></a><a id="stor_map_all_buffers_including_read_write"></a><dl>

### -field <b>STOR_MAP_ALL_BUFFERS_INCLUDING_READ_WRITE</b>

</dl>
</td>
<td width="60%">
<p>Maps the buffer all for IO including read and write requests.</p>
<p> Miniports supporting  boot must handle a read or write request of PAGE_SIZE in length. These read or write requests must always complete  successfully.</p>
<p> Storport may fail to map the buffer under low system memory conditions. In this case, the <b>DataBuffer</b> member in the SRB will be NULL.

</p>
<p> This value is valid starting with Windows 8.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>NeedPhysicalAddresses</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the miniport driver must translate virtual addresses to physical addresses, as required by the HBA. The Storport driver initializes this member to <b>TRUE</b>, because its miniport drivers must support scatter/gather lists. Miniport must not modify this value. </p>
</dd>

### -field <b>TaggedQueuing</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the HBA supports queuing of multiple requests with SCSI tags. The Storport driver initializes this member to <b>TRUE</b>, because its miniport drivers must support tagged-queuing. Miniport drivers must not modify this value.</p>
</dd>

### -field <b>AutoRequestSense</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the HBA supports auto request sense. The Storport driver initializes this member to <b>TRUE</b>, because its miniport drivers must support auto-request sense. Miniport drivers must not modify this value. </p>
</dd>

### -field <b>MultipleRequestPerLu</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the HBA supports multiple requests per logical unit. The Storport driver initializes this member to <b>TRUE</b>, because its miniport drivers must support multiple requests issued to a logical unit at time. Miniport drivers must not modify this value. </p>
</dd>

### -field <b>ReceiveEvent</b>

<dd>
<p>The Storport driver does not use this member, and its miniport drivers must not set it. </p>
</dd>

### -field <b>RealModeInitialized</b>

<dd>
<p>The Storport driver does not use this member, and its miniport drivers must not set it. </p>
</dd>

### -field <b>BufferAccessScsiPortControlled</b>

<dd>
<p>The Storport driver does not use this member, and its miniport drivers must not set it. </p>
</dd>

### -field <b>MaximumNumberOfTargets</b>

<dd>
<p>Specifies the number of target peripherals the adapter can control. By default, the value of this member is SCSI_MAXIMUM_TARGETS_PER_BUS. A miniport driver can reset this member to a lesser value if the HBA has more limited capabilities or to a greater value, indicating that the HBA has extended bus capabilities. The maximum value for this member is 255.</p>
</dd>

### -field <b>SrbType</b>

<dd>
<p>The type of SRBs to be sent to the miniport driver. This is set to either of these values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="SRB_TYPE_SCSI_REQUEST_BLOCK"></a><a id="srb_type_scsi_request_block"></a><dl>

### -field <b>SRB_TYPE_SCSI_REQUEST_BLOCK</b>

</dl>
</td>
<td width="60%">
<p>The miniport driver receives standard SRBs.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SRB_TYPE_STORAGE_REQUEST_BLOCK"></a><a id="srb_type_storage_request_block"></a><dl>

### -field <b>SRB_TYPE_STORAGE_REQUEST_BLOCK</b>

</dl>
</td>
<td width="60%">
<p>The miniport driver receives extended SRBs.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>AddressType</b>

<dd>
<p>The address type used between Storport and the miniport driver. Currently, only on address type is supported and member is  set to STORAGE_ADDRESS_TYPE_BTL8.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="STORAGE_ADDRESS_TYPE_BTL8"></a><a id="storage_address_type_btl8"></a><dl>

### -field <b>STORAGE_ADDRESS_TYPE_BTL8</b>

</dl>
</td>
<td width="60%">
<p>Bus, Target, and LUN (BTL) 8-bit addressing.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ReservedUchars</b>

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <b>SlotNumber</b>

<dd>
<p>Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.</p>
</dd>

### -field <b>BusInterruptLevel2</b>

<dd>
<p>Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.</p>
</dd>

### -field <b>BusInterruptVector2</b>

<dd>
<p>Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.</p>
</dd>

### -field <b>InterruptMode2</b>

<dd>
<p>Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.</p>
</dd>

### -field <b>DmaChannel2</b>

<dd>
<p>Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.</p>
</dd>

### -field <b>DmaPort2</b>

<dd>
<p>Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.</p>
</dd>

### -field <b>DmaWidth2</b>

<dd>
<p>Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.</p>
</dd>

### -field <b>DmaSpeed2</b>

<dd>
<p>Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.</p>
</dd>

### -field <b>DeviceExtensionSize</b>

<dd>
<p>Specifies the size, in bytes, required by the miniport driver for its per-adapter device extension. A miniport driver uses its device extension as storage for driver-determined host bus adapter (HBA) information. The operating system-specific port driver initializes each device extension one time, when it first allocates the extension, and fills it with zeros. It passes a pointer to the HBA-specific device extension in every call to a miniport driver. The given size does not include any miniport driver-requested per-logical-unit storage. The size of per-logical-unit storage is specified via the <b>SpecificLuExtensionSize</b> field, described later in this topic.</p>
<p>Although SCSIPort re-initializes the device extension whenever the adapter is stopped and thus subsequent calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557300">HwScsiFindAdapter</a> receive a zeroed-out device extension, Storport does not follow that model. Rather, Storport resets the device extension to zero only when it is first allocated, so only the first call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> for a given adapter receives a zeroed-out device extension. Subsequent calls to <b>HwStorFindAdapter</b> and other miniport functions receive the device extension as last modified by the miniport driver. This allows the miniport driver to maintain knowledge about the state of the adapter between Plug and Play (PnP) stops and restarts, possibly enabling the miniport driver to optimize it's initialization procedure.</p>
</dd>

### -field <b>SpecificLuExtensionSize</b>

<dd>
<p>This member specifies the size in bytes required by the miniport driver for its per-logical-unit-storage, if any, to handle data transfers larger than 64K. The Storport driver initializes this member to the value in the same member of the <a href="storage.hw_initialization_data__storport_">HW_INITIALIAZATION_DATA</a> structure sent in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567108">StorPortInitialize</a> routine.  Set this member to zero if the miniport driver does not maintain per-LU information for which it requires storage. This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff567103">StorPortGetUncachedExtension</a>
</p>
</dd>

### -field <b>SrbExtensionSize</b>

<dd>
<p>Specifies the size in bytes required by the miniport driver for its per-request storage, if any, to handle data transfers larger than 64K.  The Storport driver initializes this member to the value in the same member of the <a href="storage.hw_initialization_data__storport_">HW_INITIALIAZATION_DATA</a> structure sent in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567108">StorPortInitialize</a> routine. Set this member before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff567103">StorPortGetUncachedExtension</a> to change the size of per-request storage based on <b>NumberOfPhysicalBreaks</b>. Set this member to zero if the miniport driver does not maintain per-SRB information for which it requires storage. This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as <b>StorPortGetUncachedExtension</b></p>
</dd>

### -field <b>Dma64BitAddresses</b>

<dd>
<p>Indicates whether the HBA is able to access addresses greater than 4 GB. Storport adapters are required to support bus-width DMA. Therefore, on a 64-bit or PAE machine, the Storport driver initializes this member to <b>SCSI_DMA64_SYSTEM_SUPPORTED</b> indicating that the adapter can access the full range of addresses. When miniport drivers detect this value, they must return one of the values in the following table in the same member to indicate to the port driver that the miniport driver supports 64-bit DMA. If the miniport fails to do this, it might severely degrade the performance of the adapter. </p>
<div class="alert"><b>Note</b>  If the device hardware supports only 32 bit addresses, then <b>Dma64BitAddresses</b> must be set to 0.</div>
<div> </div>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="SCSI_DMA64_MINIPORT_SUPPORTED"></a><a id="scsi_dma64_miniport_supported"></a><dl>

### -field <b>SCSI_DMA64_MINIPORT_SUPPORTED</b>

</dl>
</td>
<td width="60%">
<p>The miniport driver supports 64-bit physical addresses for I/O transfers.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SCSI_DMA64_MINIPORT_FULL64BIT_SUPPORTED"></a><a id="scsi_dma64_miniport_full64bit_supported"></a><dl>

### -field <b>SCSI_DMA64_MINIPORT_FULL64BIT_SUPPORTED</b>

</dl>
</td>
<td width="60%">
<p>The miniport driver supports full 64-bit addressing. This indicates that I/O requests
may have physical addresses &gt; 4GB. The uncached extension,
SenseInfo, and Srb Extension may exist above 4GB.
Allocations are restricted to 4GB boundary alignment in order to prevent them from crossing a 4GB boundary.
</p>
<p>This option is defined starting with Windows Server 2003 with SP1. This option is enabled starting in Windows 7 with Hotfix KB2468345 or Windows 7 with SP1 with Hotfix KB2468345.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SCSI_DMA64_MINIPORT_FULL64BIT_NO_BOUNDARY_REQ_SUPPORTED"></a><a id="scsi_dma64_miniport_full64bit_no_boundary_req_supported"></a><dl>

### -field <b>SCSI_DMA64_MINIPORT_FULL64BIT_NO_BOUNDARY_REQ_SUPPORTED</b>

</dl>
</td>
<td width="60%">
<p>The miniport driver supports full 64-bit addressing. This indicates that I/O requests
may have physical addresses &gt; 4GB. The uncached extension,
SenseInfo, and Srb Extension may exist above 4GB.
Allocations have no boundary alignment requirement.
</p>
<p>This option is available in starting with Windows 8.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SCSI_DMA64_MINIPORT_64BIT_ONE_4GB_SUPPORTED"></a><a id="scsi_dma64_miniport_64bit_one_4gb_supported"></a><dl>

### -field <b>SCSI_DMA64_MINIPORT_64BIT_ONE_4GB_SUPPORTED</b>

</dl>
</td>
<td width="60%">
<p>The miniport driver support 64-bit addressing in a single 4GB region. This indicates that
I/O requests, uncached extension, <b>SenseInfo</b>, and <b>SrbExtension</b> may have physical addresses &gt; 4GB in a single 4GB region.</p>
<p>This option is available in starting with Windows 8.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ResetTargetSupported</b>

<dd>
<p>Obsolete. Do not use this member.</p>
</dd>

### -field <b>MaximumNumberOfLogicalUnits</b>

<dd>
<p>Specifies the maximum number of logical units per target the HBA can control. By default, the value of this member is SCSI_MAXIMUM_LOGICAL_UNITS. A miniport driver can reset this member to a lesser value if the HBA has more limited capabilities or to a greater value, indicating that the HBA has extended  capabilities. The maximum value for this member is SCSI_MAXIMUM_LUNS_PER_TARGET.</p>
</dd>

### -field <b>WmiDataProvider</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the miniport driver responds to Windows Management Instrumentation (WMI) requests. The Storport driver initializes this member to <b>TRUE</b>, because its miniport drivers must support WMI. Additionally, miniport drivers for fibre channel adapters are expected to support the SAN Management HBA API through WMI, and miniport drivers for host-based RAID adapters are required to support the RAID Management Interface. </p>
<p>Miniport drivers must not modify this value.</p>
</dd>

### -field <b>SynchronizationModel</b>

<dd>
<p>Specifies the I/O synchronization model the miniport driver supports. The possible values are as follows:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>StorSynchronizeFullDuplex</b></p>
</td>
<td>
<p>Full-duplex mode. </p>
</td>
</tr>
<tr>
<td>
<p><b>StorSynchronizeHalfDuplex</b></p>
</td>
<td>
<p>Half-duplex mode. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>HwMSInterruptRoutine</b>

<dd>
<p>A pointer to the miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff557268">HwMSInterruptRoutine</a>. This is a required routine for any miniport driver of an HBA that generates message signaled interrupts (MSIs). A miniport driver sets this member to <b>NULL</b> if the HBA does not generate MSIs.</p>
</dd>

### -field <b>InterruptSynchronizationMode</b>

<dd>
<p>A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff559199">INTERRUPT_SYNCHRONIZATION_MODE</a> that specifies the interrupt synchronization mode. The interrupt synchronization mode determines how the port driver synchronizes message signaled interrupts.</p>
</dd>

### -field <b>DumpRegion</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff562235">MEMORY_REGION</a> that describes a region of physically contiguous memory that miniport drivers can use during a crash dump or hibernation.</p>
</dd>

### -field <b>RequestedDumpBufferSize</b>

<dd>
<p>Size of the uncached extension to be allocated for use during dump/hibernation.</p>
</dd>

### -field <b>VirtualDevice</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that there is no real hardware behind this device (for example, no DMA object, interrupt, I/O ports). Storport behaves differently in some circumstances when it supports a "virtual" miniport instead of a miniport that is controlling real hardware.</p>
</dd>

### -field <b>DumpMode</b>

<dd>
<p>A value indicating the use of the miniport during dump mode. This member is included starting with Windows 8. It can have one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="DUMP_MODE_CRASH"></a><a id="dump_mode_crash"></a><dl>

### -field <b>DUMP_MODE_CRASH</b>

</dl>
</td>
<td width="60%">
<p>The  miniport in dump mode is used for a crashdump.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DUMP_MODE_HIBER"></a><a id="dump_mode_hiber"></a><dl>

### -field <b>DUMP_MODE_HIBER</b>

</dl>
</td>
<td width="60%">
<p>The  miniport in dump mode is used for a hibernation.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DUMP_MODE_MARK_MEMORY"></a><a id="dump_mode_mark_memory"></a><dl>

### -field <b>DUMP_MODE_MARK_MEMORY</b>

</dl>
</td>
<td width="60%">
<p>The  miniport in dump mode is used for marking required memory.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DUMP_MODE_RESUME"></a><a id="dump_mode_resume"></a><dl>

### -field <b>DUMP_MODE_RESUME</b>

</dl>
</td>
<td width="60%">
<p>The  miniport in dump mode is used for a resume from hibernation.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ExtendedFlags1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>MaxNumberOfIO</b>

<dd>
<p>The maximum number of outstanding I/O operations supported by the HBA. The default is set to 1000 by Storport. If the HBA does not support 1000 outstanding I/O operations, the miniport should adjust this to an appropriate smaller value.</p>
<p>  If the HBA can support more than 1000 outstanding I/O operations, this value can increase to any value supported by the adapter hardware. To allow more than 1000 outstanding I/O operations, the HBA must support, and set in <b>Dma64BitAddresses</b>, to one the following 64 bit DMA addressing methods.</p>
<ul>
<li>SCSI_DMA64_MINIPORT_FULL64BIT_SUPPORTED</li>
<li>SCSI_DMA64_MINIPORT_FULL64BIT_NO_BOUNDARY_REQ_SUPPORTED</li>
<li>SCSI_DMA64_MINIPORT_64BIT_ONE_4GB_SUPPORTED</li>
</ul>
<p>Prior to Windows 8, this member is reserved.</p>
</dd>

### -field <b>MaxIOsPerLun</b>

<dd>
<p>The maximum number of I/O requests supported on a LUN. The Storport driver will set this to a default value of 255. If a LUN does not support 255 outstanding I/O requests, the miniport should adjust this to an appropriate smaller value. This member must be &lt;= <b>MaxNumberOfIO</b>.</p>
<div class="alert"><b>Note</b>  <b>SrbType</b> must contain <b>SRB_TYPE_STORAGE_REQUEST_BLOCK</b> to support <b>MaxIOsPerLun</b> &gt; 255.</div>
<div> </div>
</dd>

### -field <b>InitialLunQueueDepth</b>

<dd>
<p>The initial LUN I/O queue depth. Storport set this to a default value of 20 for physical miniports and to 250 for virtual miniports. This member adjusts the initial queue depth for all LUNs on the adapter. The queue depth for an individual LUN is set by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff567506">StorPortSetDeviceQueueDepth</a>. This member is typically set to the same value as <b>MaxIOsPerLun</b>.</p>
</dd>

### -field <b>BusResetHoldTime</b>

<dd>
<p>The amount of time, in microseconds, to pause the adapter after a reset is detected. Set this value to 0 if no wait time is needed after a bus reset.</p>
</dd>

### -field <b>FeatureSupport</b>

<dd>
<p>Storport features requested for the adapter.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="STOR_ADAPTER_FEATURE_RESERVED"></a><a id="stor_adapter_feature_reserved"></a><dl>

### -field <b>STOR_ADAPTER_FEATURE_RESERVED</b>

</dl>
</td>
<td width="60%">
<p>System reserved features are supported. Miniports must not set this feature.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STOR_ADAPTER_FEATURE_STOP_UNIT_DURING_POWER_DOWN"></a><a id="stor_adapter_feature_stop_unit_during_power_down"></a><dl>

### -field <b>STOR_ADAPTER_FEATURE_STOP_UNIT_DURING_POWER_DOWN</b>

</dl>
</td>
<td width="60%">
<p>The adapter receives the STOP_UNIT command during system shutdown.</p>
</td>
</tr>
</table>
<p> </p>
<p>Prior to Windows 8, this member is reserved and must be set to 0.</p>
</dd>
</dl>

## -remarks
<p>When the PnP Manager notifies the Storport driver to start a device, Storport allocates and initializes this structure, supplies as much HBA-specific configuration information as possible, and passes the structure to the miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> routine. </p>

<p>The Storport driver does not support non-PnP devices, so <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> does not search for the adapter. Its principal function is to initialize the <b>PORT_CONFIGURATION_INFORMATION</b> structure. </p>

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
<a href="storage.hw_initialization_data__storport_">HW_INITIALIAZATION_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562235">MEMORY_REGION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567023">StorPortAcquireMSISpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567090">StorPortGetMSIInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567494">StorPortReleaseMSISpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567506">StorPortSetDeviceQueueDepth</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20PORT_CONFIGURATION_INFORMATION structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
