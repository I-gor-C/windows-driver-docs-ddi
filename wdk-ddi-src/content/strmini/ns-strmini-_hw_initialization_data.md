---
UID: NS:strmini._HW_INITIALIZATION_DATA
title: "_HW_INITIALIZATION_DATA"
author: windows-driver-content
description: Each SCSI miniport driver's DriverEntry routine must initialize with zeros and, then, fill in the relevant HW_INITIALIZATION_DATA (SCSI) information for the OS-specific port driver.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
old-location: storage\hw_initialization_data__scsi_.htm
old-project: storage
ms.assetid: 58c80d37-a40d-4839-b516-a78720860cbc
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PHW_INITIALIZATION_DATA, HW_INITIALIZATION_DATA, HW_INITIALIZATION_DATA structure [Storage Devices], PHW_INITIALIZATION_DATA, PHW_INITIALIZATION_DATA structure pointer [Storage Devices], _HW_INITIALIZATION_DATA, _HW_INITIALIZATION_DATA structure [Storage Devices], srb/HW_INITIALIZATION_DATA, srb/PHW_INITIALIZATION_DATA, storage.hw_initialization_data__scsi_, structs-scsiport_4d9f09a8-742b-4c72-8fc5-dd968bd990d6.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: strmini.h
req.include-header: Srb.h, Strmini.h
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
-	HW_INITIALIZATION_DATA
product: Windows
targetos: Windows
req.typenames: HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA
req.product: Windows 10 or later.
---

# _HW_INITIALIZATION_DATA structure
Each SCSI miniport driver's <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> routine must initialize with zeros and, then, fill in the relevant HW_INITIALIZATION_DATA (SCSI) information for the OS-specific port driver.
<div class="alert"><b>Note</b>  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-driver">Storport driver</a> and <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-miniport-drivers">Storport miniport</a> driver models.</div><div> </div>

## Syntax
````
typedef struct _HW_INITIALIZATION_DATA {
  ULONG             HwInitializationDataSize;
  INTERFACE_TYPE    AdapterInterfaceType;
  PHW_INITIALIZE    HwInitialize;
  PHW_STARTIO       HwStartIo;
  PHW_INTERRUPT     HwInterrupt;
  PHW_FIND_ADAPTER  HwFindAdapter;
  PHW_RESET_BUS_BUS HwResetBus;
  PHW_DMA_STARTED   HwDmaStarted;
  PHW_ADAPTER_STATE HwAdapterState;
  ULONG             DeviceExtensionSize;
  ULONG             SpecificLuExtensionSize;
  ULONG             SrbExtensionSize;
  ULONG             NumberOfAccessRanges;
  PVOID             Reserved;
  BOOLEAN           MapBuffers;
  BOOLEAN           NeedPhysicalAddresses;
  BOOLEAN           TaggedQueuing;
  BOOLEAN           AutoRequestSense;
  BOOLEAN           MultipleRequestPerLu;
  BOOLEAN           ReceiveEvent;
  USHORT            VendorIdLength;
  PVOID             VendorId;
  USHORT            ReservedUshort;
  USHORT            DeviceIdLength;
  PVOID             DeviceId;
  PHW_STOP_ADAPTER  HwAdapterControl;
} HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA;
````

## Members


`BufferAlignment`



`BusMasterDMA`



`DeviceExtensionSize`

Specifies the size in bytes required by the miniport driver for its per-HBA device extension. A miniport driver uses its device extension as storage for driver-determined HBA information. The OS-specific port driver initializes each device extension it allocates with zeros, and passes a pointer to the HBA-specific device extension in every call to a miniport driver except to its <b>DriverEntry</b> routine. The given size does not include any miniport driver-requested per-logical-unit storage, described next.

`Dma24BitAddresses`



`DmaBufferSize`



`FilterInstanceExtensionSize`



`HwCancelPacket`



`HwInitializationDataSize`

Specifies the size of this structure in bytes, as returned by <b>sizeof</b>(). In effect, this member indicates the version of this structure being used by the miniport driver. A miniport driver's <b>DriverEntry</b> routine should set this member's value for the port driver.

`HwInterrupt`

Pointer to the miniport driver's <a href="..\strmini\nc-strmini-phw_interrupt.md">HwScsiInterrupt</a> routine, which is a required entry point for any miniport driver of an HBA that generates interrupts. Set this to <b>NULL</b> if the miniport driver needs no ISR. The prototype for this routine is <a href="..\strmini\nc-strmini-phw_interrupt.md">PHW_INTERRUPT</a>.

`HwReceivePacket`



`HwRequestTimeoutHandler`



`NameExtensionArray`



`NumNameExtensions`



`PerRequestExtensionSize`



`PerStreamExtensionSize`



`Reserved`

Reserved for system use and not available for use by miniport drivers.

`TurnOffSynchronization`



## Remarks
Each miniport driver must initialize the HW_INITIALIZATION_DATA structure with zeros before it sets the values of relevant members in this structure and calls <b>ScsiPortInitialize</b>.

The <b>Dma64BitAddresses</b> member of HW_INITIALIZATION_DATA has been eliminated in Windows 2000 (See the discussion under PORT_CONFIGURATION_DATA for further details).

Both HW_INITIALIZATION_DATA and PORT_CONFIGURATION_INFORMATION have a pair of members called <b>SpecificLuExtensionSize</b> and <b>SrbExtensionSize</b> whose values are handled differently than they were prior to Windows 2000. The miniport driver must calculate the initial values of <b>SpecificLuExtensionSize</b> and <b>SrbExtensionSize</b> in HW_INITIALIZATION_DATA based on the assumption that the HBA is capable of handling 32-bit addresses, regardless of what the controller can actually support. (See the discussion under PORT_CONFIGURATION_DATA for further details.)

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | strmini.h (include Srb.h, Strmini.h) |

## See Also

<a href="..\minitape\ns-minitape-_scsi_request_block.md">SCSI_REQUEST_BLOCK</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552654">DriverEntry of SCSI Miniport Driver</a>



<a href="..\srb\nc-srb-phw_initialize.md">HwScsiInitialize</a>



<a href="..\srb\nf-srb-scsiportinitialize.md">ScsiPortInitialize</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20_HW_INITIALIZATION_DATA structure%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>