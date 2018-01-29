---
UID : NS:srb._STORAGE_REQUEST_BLOCK
title : _STORAGE_REQUEST_BLOCK
author : windows-driver-content
description : The STORAGE_REQUEST_BLOCK is the extended format SCSI Request Block (SRB) structure.
old-location : storage\storage_request_block.htm
old-project : storage
ms.assetid : 67A5077D-B1AD-49B7-B024-D139E375483F
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : SRB_FLAGS_IS_ACTIVE, SRB_FLAGS_BYPASS_FROZEN_QUEUE, SRB_STATUS_PENDING, SRB_STATUS_UNEXPECTED_BUS_FREE, SRB_STATUS_INVALID_PATH_ID, SRB_STATUS_NOT_POWERED, SRB_FUNCTION_RESET_BUS, SRB_STATUS_INVALID_LUN, SRB_FUNCTION_LOCK_QUEUE, SRB_STATUS_REQUEST_SENSE_FAILED, SRB_FUNCTION_WMI, STORAGE_REQUEST_BLOCK, SRB_FUNCTION_RELEASE_RECOVERY, SRB_STATUS_TIMEOUT, SRB_STATUS_ABORTED, SRB_FUNCTION_EXECUTE_SCSI, SRB_FUNCTION_RESET_LOGICAL_UNIT, SRB_STATUS_ERROR_RECOVERY, SRB_FLAGS_DATA_IN, _STORAGE_REQUEST_BLOCK, SRB_STATUS_INTERNAL_ERROR, SRB_STATUS_ABORT_FAILED, SRB_STATUS_NO_DEVICE, SRB_FLAGS_BYPASS_LOCKED_QUEUE, PSTORAGE_REQUEST_BLOCK structure pointer [Storage Devices], SRB_STATUS_REQUEST_FLUSHED, SRB_STATUS_QUEUE_FROZEN, SRB_FUNCTION_FLUSH, SRB_FLAGS_D3_PROCESSING, SRB_FLAGS_NO_DATA_TRANSFER, SRB_STATUS_BUS_RESET, SRB_FLAGS_DISABLE_AUTOSENSE, SRB_FUNCTION_ABORT_COMMAND, SRB_FUNCTION_QUIESCE_DEVICE, SRB_FLAGS_SGLIST_FROM_POOL, SRB_STATUS_SELECTION_TIMEOUT, SRB_STATUS_INVALID_REQUEST, SRB_FLAGS_FREE_SENSE_BUFFER, SRB_FLAGS_ADAPTER_CACHE_ENABLE, storport/STORAGE_REQUEST_BLOCK, SRB_FUNCTION_PNP, SRB_FUNCTION_RESET_DEVICE, SRB_FLAGS_DATA_OUT, SRB_STATUS_PHASE_SEQUENCE_FAILURE, storport/PSTORAGE_REQUEST_BLOCK, SRB_STATUS_COMMAND_TIMEOUT, SRB_FLAGS_DISABLE_SYNCH_TRANSFER, SRB_FLAGS_NO_QUEUE_FREEZE, SRB_FUNCTION_SHUTDOWN, PSTORAGE_REQUEST_BLOCK, SRB_FUNCTION_RECEIVE_EVENT, SRB_STATUS_AUTOSENSE_VALID, SRB_STATUS_BAD_SRB_BLOCK_LENGTH, SRB_FUNCTION_UNLOCK_QUEUE, SRB_STATUS_BAD_FUNCTION, SRB_FLAGS_UNSPECIFIED_DIRECTION, storage.storage_request_block, SRB_FUNCTION_FREE_DUMP_POINTERS, SRB_FLAGS_ALLOCATED_FROM_ZONE, SRB_STATUS_NO_HBA, SRB_STATUS_SUCCESS, SRB_FLAGS_QUEUE_ACTION_ENABLE, SRB_FLAGS_DISABLE_DISCONNECT, SRB_STATUS_BUSY, SRB_STATUS_MESSAGE_REJECTED, SRB_STATUS_LINK_DOWN, SRB_FUNCTION_IO_CONTROL, STORAGE_REQUEST_BLOCK structure [Storage Devices], SRB_FUNCTION_CRYPTO_OPERATION, SRB_STATUS_ERROR, SRB_FLAGS_NO_KEEP_AWAKE, SRB_FUNCTION_POWER, SRB_STATUS_DATA_OVERRUN, SRB_STATUS_PARITY_ERROR, SRB_STATUS_INVALID_TARGET_ID, SRB_FUNCTION_TERMINATE_IO, SRB_FUNCTION_DUMP_POINTERS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : srb.h
req.include-header : Storport.h, Srb.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 8 and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PSTORAGE_REQUEST_BLOCK, STORAGE_REQUEST_BLOCK
req.product : Windows 10 or later.
---

# _STORAGE_REQUEST_BLOCK structure
The <b>STORAGE_REQUEST_BLOCK</b> is the extended format SCSI Request Block (SRB) structure. The structure provides for the addition of extended data associated with an SRB function.
<div class="alert"><b>Note</b>  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-driver">Storport driver</a> and <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-miniport-drivers">Storport miniport</a> driver models.</div><div> </div>

## Syntax
````
typedef struct _STORAGE_REQUEST_BLOCK {
  USHORT                        Length;
  UCHAR                         Function;
  UCHAR                         SrbStatus;
  UCHAR                         ReservedUchar[4];
  ULONG                         Signature;
  ULONG                         Version;
  ULONG                         SrbLength;
  ULONG                         SrbFunction;
  ULONG                         SrbFlags;
  ULONG                         ReservedUlong;
  ULONG                         RequestTag;
  USHORT                        RequestPriority;
  USHORT                        RequestAttribute;
  ULONG                         TimeOutValue;
  ULONG                         SystemStatus;
  ULONG                         ZeroGuard1;
  ULONG                         AddressOffset;
  ULONG                         NumSrbExData;
  ULONG                         DataTransferLength;
  PVOID                         DataBuffer;
  PVOID                         ZeroGuard2;
  PVOID                         OriginalRequest;
  PVOID                         ClassContext;
  PVOID                         PortContext;
  PVOID                         MiniportContext;
  struct _STORAGE_REQUEST_BLOCK  *NextSrb;
  ULONG                         SrbExDataOffset[ANYSIZE_ARRAY];
} STORAGE_REQUEST_BLOCK, *PSTORAGE_REQUEST_BLOCK;
````

## Members


`_STORAGE_REQUEST_BLOCK`



`AddressOffset`

The offset of the storage request address from the beginning of this structure. This offset locates a <a href="..\storport\ns-storport-_stor_address.md">STOR_ADDRESS</a> structure that contains the address for the request.

`ClassContext`

Points to a class driver context data for this request. This member is irrelevant to miniport drivers.

`DataBuffer`

Points to the data buffer. Miniport drivers should not use this value as a data pointer unless the miniport driver set <b>MapBuffers</b> to <b>TRUE</b> in the <a href="..\strmini\ns-strmini-_port_configuration_information.md">PORT_CONFIGURATION_INFORMATION</a> for the HBA. In the case of SRB_FUNCTION_IO_CONTROL requests, however, miniport drivers can use this value as a data pointer regardless of the value of <b>MapBuffers</b>.

`DataTransferLength`

Indicates the size, in bytes, of the data buffer. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred.

`Function`

Set to <b>SRB_FUNCTION_STORAGE_REQUEST_BLOCK</b> to indicate that this is an extended SRB. Unlike in <a href="..\srb\ns-srb-_scsi_request_block.md">SCSI_REQUEST_BLOCK</a>, the SRB function identifier is in the <b>SrbFunction</b> member instead.

`Length`

Specifies the size of the SRB header for compatibility with the <a href="..\srb\ns-srb-_scsi_request_block.md">SCSI_REQUEST_BLOCK</a> structure. This is equal to the offset of the <b>Signature</b> member of this structure.

`MiniportContext`

Points to the Srb extension. A miniport driver must not use this member if it set <b>SrbExtensionSize</b> to zero in  <a href="..\storport\ns-storport-_hw_initialization_data.md">HW_INITIALIZATION_DATA</a>. The memory at <b>MiniportContext</b> is not initialized by the operating system-specific port driver, and the miniport driver-determined data can be accessed directly by the HBA. The corresponding physical address can be obtained by calling <a href="..\storport\nf-storport-storportgetphysicaladdress.md">StorportGetPhysicalAddress</a> with the <b>MiniportContext</b> pointer.

`NextSrb`

Indicates the <b>STORAGE_REQUEST_BLOCK</b> to which this request applies. Only a small subset of requests use a second SRB, for example SRB_FUNCTION_ABORT_COMMAND.

`NumSrbExData`

The count of extended SRB data blocks for this request.

`OriginalRequest`

Points to the IRP for this request. This member is irrelevant to miniport drivers.

`PortContext`

Points to a port driver context data for this request. This member is irrelevant to miniport drivers.

`RequestAttribute`

Indicates the tagged-queuing message to be used when the <b>SRB_FLAGS_QUEUE_ACTION_ENABLE</b> flag is set. The value can be one of the following: <b>SRB_SIMPLE_TAG_REQUEST</b>, <b>SRB_HEAD_OF_QUEUE_TAG_REQUEST</b>, or <b>SRB_ORDERED_QUEUE_TAG_REQUEST</b>.

`RequestPriority`

The priority assignment for the SRB.

`RequestTag`

Contains the queue-tag value assigned by the operating system-specific port driver. If this member is used for tagged queuing, the HBA supports internal queuing of requests to logical units (LUs) and the miniport driver set <b>TaggedQueueing</b> to <b>TRUE</b> in the PORT_CONFIGURATION_INFORMATION for this HBA.

`ReservedUchar`

Reserved. Set to 0.

`ReservedUlong`

Reserved. Set to 0.

`Signature`

The signature of the extended SRB format. This is set to SRB_SIGNATURE.

`SrbExDataOffset`

An array of offsets specifying the location of extended data blocks for the SRB. This array is empty if <b>NumSrbExData</b> = 0.

`SrbFlags`

Indicates various parameters and options for the request. <b>SrbFlags</b> is read-only, except when <b>SRB_FLAGS_UNSPECIFIED_DIRECTION</b> is set and miniport drivers of subordinate DMA adapters are required to update <b>SRB_FLAGS_DATA_IN</b> or <b>SRB_FLAGS_DATA_OUT</b>. This member can have one or more of these flags set:

`SrbFunction`

Specifies the operation to be performed, which can be one of these values:

`SrbLength`

The length of this extended SRB, in bytes, including this structure, address and any SRB extended data.

`SrbStatus`

Returns the status of the completed request. This member should be set by the miniport driver before it notifies the operating system-specific driver that the request has completed by calling <a href="..\storport\nf-storport-storportnotification.md">StorPortNotification</a> with <b>RequestComplete</b>. The value of this member can be one of the following:

`SystemStatus`

Used by the Storport driver, instead of <b>SrbStatus</b>, to report the status of the completed request whenever the request cannot be delivered to the miniport driver. In such cases, <b>SrbStatus</b> is set to <b>SRB_STATUS_INTERNAL_ERROR</b>. This member is used exclusively for communication between the Storport and the class driver and should not be used by miniport drivers.

`TimeOutValue`

Indicates the interval, in seconds, that the request can execute before the operating system-specific port driver might consider it timed out. Miniport drivers are not required to time requests because the port driver already does.

`Version`

The version of the structure used. The current version is <b>STORAGE_REQUEST_BLOCK_VERSION_1</b>.

`ZeroGuard1`

A guard area to protect against drivers that interpret this structure as <a href="..\srb\ns-srb-_scsi_request_block.md">SCSI_REQUEST_BLOCK</a>. Set to 0.

`ZeroGuard2`

A guard area to protect against drivers that interpret this structure as <a href="..\srb\ns-srb-_scsi_request_block.md">SCSI_REQUEST_BLOCK</a>. Set to 0.

## Remarks
Starting in Windows 8, an extended  SRB type is supported with the use of the <b>STORAGE_REQUEST_BLOCK</b> structure. <b>STORAGE_REQUEST_BLOCK</b> extends SRB functions, allowing extended data blocks for the SRB function to be added to the request. Support for SRB requests using the <a href="..\srb\ns-srb-_scsi_request_block.md">SCSI_REQUEST_BLOCK</a> structure will continue.

If <b>NumSrbExData</b> &gt; 0, the offsets for the SRB extended data blocks are in the  <b>SrbExDataOffset</b> array. Each offset is relative to the beginning of this structure and points to a <a href="..\storport\ns-storport-_srbex_data.md">SRBEX_DATA</a> structure containing the extended data block.

The target device address for the SRB is in a <a href="..\storport\ns-storport-_stor_address.md">STOR_ADDRESS</a> structure indicated by <b>AddressOffset</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | srb.h (include Storport.h, Srb.h) |

## See Also

<a href="..\srb\ns-srb-_scsi_request_block.md">SCSI_REQUEST_BLOCK</a>

<a href="..\storport\ns-storport-_stor_address.md">STOR_ADDRESS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_REQUEST_BLOCK structure%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>