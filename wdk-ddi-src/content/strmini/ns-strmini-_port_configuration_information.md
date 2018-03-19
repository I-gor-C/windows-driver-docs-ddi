---
UID: NS:strmini._PORT_CONFIGURATION_INFORMATION
title: "_PORT_CONFIGURATION_INFORMATION"
author: windows-driver-content
description: PORT_CONFIGURATION_INFORMATION (SCSI) contains configuration information for an HBA.
old-location: storage\port_configuration_information__scsi_.htm
old-project: storage
ms.assetid: f3c9d851-d30d-4757-82a3-225ee67528c1
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PPORT_CONFIGURATION_INFORMATION, PORT_CONFIGURATION_INFORMATION, PORT_CONFIGURATION_INFORMATION structure [Storage Devices], PPORT_CONFIGURATION_INFORMATION, PPORT_CONFIGURATION_INFORMATION structure pointer [Storage Devices], _PORT_CONFIGURATION_INFORMATION, _PORT_CONFIGURATION_INFORMATION structure [Storage Devices], srb/PPORT_CONFIGURATION_INFORMATION, srb/_PORT_CONFIGURATION_INFORMATION, storage.port_configuration_information__scsi_, structs-scsiport_1a472219-5839-443c-a3a1-26c9708b3b18.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: strmini.h
req.include-header: Srb.h, Storport.h, Strmini.h
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
-	srb.h
api_name:
-	PORT_CONFIGURATION_INFORMATION
product: Windows
targetos: Windows
req.typenames: PORT_CONFIGURATION_INFORMATION, *PPORT_CONFIGURATION_INFORMATION
req.product: Windows 10 or later.
---

# _PORT_CONFIGURATION_INFORMATION structure
PORT_CONFIGURATION_INFORMATION (SCSI) contains configuration information for an HBA. The OS-specific port driver allocates and initializes this structure, supplies as much HBA-specific configuration information as possible, and passes the structure to the miniport driver's <i>HwScsiFindAdapter</i> routine. The port driver gets some of the information for this structure from the miniport driver's HW_INITIALIZATION_DATA structure. The miniport driver's <i>HwScsiFindAdapter</i> routine is responsible for determining whether the miniport driver can support the HBA and, if so, for filling in the pertinent remaining information in the PORT_CONFIGURATION_INFORMATION structure.
<div class="alert"><b>Note</b>  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-driver">Storport driver</a> and <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-miniport-drivers">Storport miniport</a> driver models.</div><div> </div>

## Syntax
````
typedef struct _PORT_CONFIGURATION_INFORMATION {
  ULONG           Length;
  ULONG           SystemIoBusNumber;
  INTERFACE_TYPE  AdapterInterfaceType;
  ULONG           BusInterruptLevel;
  ULONG           BusInterruptVector;
  KINTERRUPT_MODE InterruptMode;
  ULONG           MaximumTransferLength;
  ULONG           NumberOfPhysicalBreaks;
  ULONG           DmaChannel;
  ULONG           DmaPort;
  DMA_WIDTH       DmaWidth;
  DMA_SPEED       DmaSpeed;
  ULONG           AlignmentMask;
  ULONG           NumberOfAccessRanges;
  ACCESS_RANGE    (*AccessRanges)[];
  PVOID           Reserved;
  UCHAR           NumberOfBuses;
  UCHAR           InitiatorBusId[8];
  BOOLEAN         ScatterGather;
  BOOLEAN         Master;
  BOOLEAN         CachesData;
  BOOLEAN         AdapterScansDown;
  BOOLEAN         AtdiskPrimaryClaimed;
  BOOLEAN         AtdiskSecondaryClaimed;
  BOOLEAN         Dma32BitAddresses;
  BOOLEAN         DemandMode;
  BOOLEAN         MapBuffers;
  BOOLEAN         NeedPhysicalAddresses;
  BOOLEAN         TaggedQueuing;
  BOOLEAN         AutoRequestSense;
  BOOLEAN         MultipleRequestPerLu;
  BOOLEAN         ReceiveEvent;
  BOOLEAN         RealModeInitialized;
  BOOLEAN         BufferAccessScsiPortControlled;
  UCHAR           MaximumNumberOfTargets;
  UCHAR           ReservedUchars[2];
  ULONG           SlotNumber;
  ULONG           BusInterruptLevel2;
  ULONG           BusInterruptVector2;
  KINTERRUPT_MODE InterruptMode2;
  ULONG           DmaChannel2;
  ULONG           DmaPort2;
  DMA_WIDTH       DmaWidth2;
  DMA_SPEED       DmaSpeed2;
  ULONG           DeviceExtensionSize;
  ULONG           SpecificLuExtensionSize;
  ULONG           SrbExtensionSize;
  UCHAR           Dma64BitAddresses;
  BOOLEAN         ResetTargetSupported;
  UCHAR           MaximumNumberOfLogicalUnits;
  BOOLEAN         WmiDataProvider;
} PORT_CONFIGURATION_INFORMATION, *PPORT_CONFIGURATION_INFORMATION;
````

## Members


`SizeOfThisPacket`



`HwDeviceExtension`



`ClassDeviceObject`



`PhysicalDeviceObject`



`SystemIoBusNumber`

Specifies the system-assigned number of the I/O bus to which the HBA is connected. The OS-specific port driver always initializes this member. Its value is system-assigned because the platform might have several I/O buses of the given <b>AdapterInterfaceType</b>.

`AdapterInterfaceType`

Identifies the I/O bus interface. The OS-specific port driver always sets this member to the value specified by the miniport driver in the <a href="..\strmini\ns-strmini-_hw_initialization_data.md">HW_INITIALIZATION_DATA (SCSI)</a> structure.

`BusInterruptLevel`

Specifies the bus-relative interrupt request level. The OS-specific port driver makes no assumptions about the HBA's interrupt usage, so the default value is zero. Depending on the given <b>AdapterInterfaceType</b> and HBA, the value set for this member can correspond to the IRQL for the bus, such as for <b>Isa</b> and <b>MicroChannel</b> type buses. Drivers of <b>Eisa</b> HBAs must set this value to the bus-relative IRQL for the HBA if the adapter is configured for level-sensitive interrupts.

`BusInterruptVector`

Specifies the bus-relative vector returned by the HBA. The OS-specific port driver makes no assumptions about the HBA's interrupt usage, so the default value is zero. This member is irrelevant to drivers that set up the <b>BusInterruptLevel</b> member for their HBAs. It is pertinent for HBAs on types of I/O buses that use interrupt vectors, such as <b>PCIBus</b>.

`InterruptMode`

Specifies whether the HBA uses <b>LevelSensitive</b> or <b>Latched</b> (sometimes called "edge-triggered") interrupts. The OS-specific port driver initializes this member to an appropriate value for the bus and the device--for example, <b>LevelSensitive</b> for <b>PCIBus</b>. Drivers of <b>Eisa</b> HBAs must reset this value if the adapter is configured for level-sensitive interrupts, as must drivers of HBAs on I/O buses that use level-sensitive interrupts, such as <b>MicroChannel</b> type buses.

`DmaChannel`

Specifies the DMA channel used by a subordinate HBA. By default, the value of this member is SP_UNINITIALIZED_VALUE. If the HBA uses a system DMA controller and the given <b>AdapterInterfaceType</b> is any value except <b>MicroChannel</b>, the miniport driver must reset this member.

`NumberOfAccessRanges`

Specifies the number of <b>AccessRanges</b> elements in the array, described next. The OS-specific port driver always sets this member to the value passed in the HW_INITIALIZATION_DATA structure when the miniport driver called <a href="..\srb\nf-srb-scsiportinitialize.md">ScsiPortInitialize</a>.

`AccessRanges`



`StreamDescriptorSize`



`Irp`



`InterruptObject`



`DmaAdapterObject`



`RealPhysicalDeviceObject`



`Reserved`

Reserved for system use and not available for use by miniport drivers.

## Remarks
The specific members initialized depend on the HBA miniport driver and on the configuration information available to the OS-specific port driver. The OS-specific port driver sets default values in all members for which it cannot supply configuration information to the miniport driver's <i>HwScsiFindAdapter</i> routine.

All HBA miniport drivers should have at least one set of defaults to use for relevant members if the OS-specific port driver does not pass in all initialized values. 

The <i>HwScsiFindAdapter</i> routine must update all members relevant to an HBA that the driver supports.

Windows NT storage class drivers, which load later than miniport drivers, depend on the information supplied by each miniport driver's <i>HwScsiFindAdapter</i> routine to set up their subsequent I/O requests. For example, the <b>MaximumTransferLength </b>and <b>NumberOfPhysicalBreaks</b> values supplied by each miniport driver control whether a class driver must split large transfer requests into a set of partial transfers to suit the limits of the HBA.

Prior to Windows 2000, both the PORT_CONFIGURATION_INFORMATION and the HW_INITIALIZATION_DATA structures had a member called <b>Dma64BitAddresses</b>. In Windows 2000, <b>Dma64BitAddresses</b> has been eliminated from the HW_INITIALIZATION_DATA structure, and its definition has changed somewhat in PORT_CONFIGURATION_INFORMATION. The port driver no longer consults HW_INITIALIZATION_DATA in order to initialize <b>Dma64BitAddresses</b> in PORT_CONFIGURATION_INFORMATION.

The <b>Dma64BitAddresses</b> member of PORT_CONFIGURATION_INFORMATION should no longer be thought of as a BOOLEAN value. A value of SCSI_DMA64_SYSTEM_SUPPORTED indicates that the port/miniport driver is required to support 64-bit addressing, but the <b>ScsiPortGetUncachedExtension</b> routine still interprets any nonzero value of <b>Dma64BitAddresses</b> as indicating that 64-bit support is required. This means that <b>ScsiPortGetUncachedExtension</b> still functions properly when called by a legacy driver that assigns BOOLEAN values to <b>Dma64BitAddresses</b>.  

In addition to <b>Dma64BitAddresses</b>, both PORT_CONFIGURATION_INFORMATION and HW_INITIALIZATION_DATA have a pair of members called <b>SpecificLuExtensionSize</b> and <b>SrbExtensionSize</b> whose values must now be handled differently. The miniport driver must calculate the initial values of <b>SpecificLuExtensionSize</b> and <b>SrbExtensionSize</b> in HW_INITIALIZATION_DATA based on the assumption that the HBA is capable of receiving 32-bit addresses, regardless of what the controller can actually support. The default values for <b>SpecificLuExtensionSize</b> and <b>SrbExtensionSize </b>in PORT_CONFIGURATION_INFORMATION will also be based on an assumption of 32-bit addressing, since the values in PORT_CONFIGURATION_INFORMATION are derived from the values in HW_INITIALIZATION_DATA.

This means that if the miniport driver needs additional space in either the LUN extension or the SRB extension in order to handle 64 bit physical addresses, it must modify the values for <b>SpecificLuExtensionSize</b> and <b>SrbExtensionSize</b> in PORT_CONFIGURATION_INFORMATION to account for this before passing PORT_CONFIGURATION_INFORMATION to <b>ScsiPortGetUncachedExtension</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | strmini.h (include Srb.h, Storport.h, Strmini.h) |

## See Also

<a href="..\strmini\ns-strmini-_hw_initialization_data.md">HW_INITIALIZATION_DATA (SCSI)</a>



<a href="..\srb\nf-srb-scsiportinitialize.md">ScsiPortInitialize</a>



<a href="..\srb\nc-srb-phw_find_adapter.md">HwScsiFindAdapter</a>



<a href="..\srb\nf-srb-scsiportgetdevicebase.md">ScsiPortGetDeviceBase</a>



<a href="..\srb\nf-srb-scsiportvalidaterange.md">ScsiPortValidateRange</a>



<a href="..\srb\nf-srb-scsiportgetuncachedextension.md">ScsiPortGetUncachedExtension</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552654">DriverEntry of SCSI Miniport Driver</a>



<a href="..\strmini\ns-strmini-_access_range.md">ACCESS_RANGE</a>