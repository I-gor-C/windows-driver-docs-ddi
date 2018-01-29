---
UID : NS:srb._SCSI_REQUEST_BLOCK
title : _SCSI_REQUEST_BLOCK
author : windows-driver-content
description : SCSI_REQUEST_BLOCK structure
old-location : storage\scsi_request_block.htm
old-project : storage
ms.assetid : ddd5180d-275c-4226-9af8-8e2ae25256e7
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : SRB_FLAGS_IS_ACTIVE, SRB_FLAGS_BYPASS_FROZEN_QUEUE, structs-scsibus_9cd58a74-3ae0-4536-ac0c-efaf73bf9733.xml, SRB_STATUS_PENDING, SRB_STATUS_UNEXPECTED_BUS_FREE, SRB_STATUS_INVALID_PATH_ID, SRB_FUNCTION_RESET_BUS, SRB_FUNCTION_LOCK_QUEUE, SRB_STATUS_INVALID_LUN, SRB_STATUS_REQUEST_SENSE_FAILED, SRB_STATUS_INVALID_TARGET_ID, _SCSI_REQUEST_BLOCK, SRB_FUNCTION_RELEASE_RECOVERY, SRB_STATUS_TIMEOUT, SRB_FUNCTION_EXECUTE_SCSI, SRB_FUNCTION_RESET_LOGICAL_UNIT, SRB_STATUS_ABORTED, SRB_STATUS_ERROR_RECOVERY, SRB_FLAGS_DATA_IN, SRB_STATUS_INTERNAL_ERROR, SRB_STATUS_ABORT_FAILED, SRB_STATUS_NO_DEVICE, SRB_FLAGS_BYPASS_LOCKED_QUEUE, PSCSI_REQUEST_BLOCK structure pointer [Storage Devices], SRB_STATUS_REQUEST_FLUSHED, storage.scsi_request_block, SRB_STATUS_QUEUE_FROZEN, SRB_FUNCTION_FLUSH, SRB_FLAGS_NO_DATA_TRANSFER, SRB_STATUS_BUS_RESET, SRB_FLAGS_DISABLE_AUTOSENSE, SRB_FUNCTION_ABORT_COMMAND, SRB_FLAGS_SGLIST_FROM_POOL, PSCSI_REQUEST_BLOCK, SRB_STATUS_SELECTION_TIMEOUT, SRB_STATUS_INVALID_REQUEST, SRB_FLAGS_FREE_SENSE_BUFFER, *PSCSI_REQUEST_BLOCK, SRB_FUNCTION_RESET_DEVICE, SRB_FLAGS_DATA_OUT, SRB_STATUS_PHASE_SEQUENCE_FAILURE, SRB_STATUS_COMMAND_TIMEOUT, SRB_FLAGS_DISABLE_SYNCH_TRANSFER, SRB_FLAGS_NO_QUEUE_FREEZE, SRB_FUNCTION_SHUTDOWN, SRB_FUNCTION_RECEIVE_EVENT, SRB_STATUS_AUTOSENSE_VALID, SRB_FUNCTION_UNLOCK_QUEUE, SRB_STATUS_BAD_FUNCTION, SRB_FLAGS_UNSPECIFIED_DIRECTION, SCSI_REQUEST_BLOCK, SRB_FUNCTION_FREE_DUMP_POINTERS, SRB_FLAGS_ALLOCATED_FROM_ZONE, SRB_STATUS_NO_HBA, SRB_STATUS_SUCCESS, srb/PSCSI_REQUEST_BLOCK, SRB_FLAGS_QUEUE_ACTION_ENABLE, SRB_STATUS_BUSY, srb/SCSI_REQUEST_BLOCK, SRB_STATUS_MESSAGE_REJECTED, SRB_FLAGS_DISABLE_DISCONNECT, SRB_FUNCTION_IO_CONTROL, SRB_FLAGS_NO_KEEP_AWAKE, SRB_STATUS_ERROR, SRB_STATUS_DATA_OVERRUN, SRB_STATUS_PARITY_ERROR, SCSI_REQUEST_BLOCK structure [Storage Devices], SRB_FUNCTION_TERMINATE_IO, SRB_FUNCTION_DUMP_POINTERS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : srb.h
req.include-header : Srb.h
req.target-type : Windows
req.target-min-winverclnt : 
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
req.typenames : SCSI_REQUEST_BLOCK, *PSCSI_REQUEST_BLOCK
req.product : Windows 10 or later.
---

# _SCSI_REQUEST_BLOCK structure
<div class="alert"><b>Note</b>  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-driver">Storport driver</a> and <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-miniport-drivers">Storport miniport</a> driver models.</div><div> </div>

## Syntax
````
typedef struct _SCSI_REQUEST_BLOCK {
  USHORT                     Length;
  UCHAR                      Function;
  UCHAR                      SrbStatus;
  UCHAR                      ScsiStatus;
  UCHAR                      PathId;
  UCHAR                      TargetId;
  UCHAR                      Lun;
  UCHAR                      QueueTag;
  UCHAR                      QueueAction;
  UCHAR                      CdbLength;
  UCHAR                      SenseInfoBufferLength;
  ULONG                      SrbFlags;
  ULONG                      DataTransferLength;
  ULONG                      TimeOutValue;
  PVOID                      DataBuffer;
  PVOID                      SenseInfoBuffer;
  struct _SCSI_REQUEST_BLOCK  *NextSrb;
  PVOID                      OriginalRequest;
  PVOID                      SrbExtension;
  union {
    ULONG InternalStatus;
    ULONG QueueSortKey;
    ULONG LinkTimeoutValue;
  };
#ifdef _WIN64
  ULONG                      Reserved;
#endif 
  UCHAR                      Cdb[16];
} SCSI_REQUEST_BLOCK, *PSCSI_REQUEST_BLOCK;
````

## Members


`_SCSI_REQUEST_BLOCK`



`Cdb`

Specifies the SCSI-2 or later command descriptor block to be sent to the target device.

`CdbLength`

Indicates the size in bytes of the SCSI-2 or later command descriptor block.

`DataBuffer`

Points to the data buffer. Miniport drivers should not use this value as a data pointer unless the miniport driver set <b>MapBuffers</b> to <b>TRUE</b> in the PORT_CONFIGURATION_INFORMATION for the HBA. In the case of SRB_FUNCTION_IO_CONTROL requests, however, miniport drivers can use this value as a data pointer regardless of the value of <b>MapBuffers</b>.

`DataTransferLength`

Indicates the size in bytes of the data buffer. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred.

`Function`

Specifies the operation to be performed, which can be one of the following values:

`Length`

Specifies the size in bytes of this structure.

`Lun`

Indicates the logical unit number of the device.

`NextSrb`

Indicates the SCSI_REQUEST_BLOCK to which this request applies. Only a small subset of requests use a second SRB, for example SRB_FUNCTION_ABORT_COMMAND.

`OriginalRequest`

Points to the IRP for this request. This member is irrelevant to miniport drivers

`PathId`

Indicates the SCSI port or bus for the request. This value is zero-based.

`QueueAction`

Indicates the tagged-queuing message to be used when the SRB_FLAGS_QUEUE_ACTION_ENABLE flag is set. The value can be one of the following: SRB_SIMPLE_TAG_REQUEST, SRB_HEAD_OF_QUEUE_TAG_REQUEST, or SRB_ORDERED_QUEUE_TAG_REQUEST, as defined according to the SCSI specification.

`QueueTag`

Contains the queue-tag value assigned by the OS-specific port driver. If this member is used for tagged queuing, the HBA supports internal queuing of requests to LUs and the miniport driver set <b>TaggedQueueing</b> to <b>TRUE</b> in the PORT_CONFIGURATION_INFORMATION for this HBA.

`Reserved`

Reserved.

`ScsiStatus`

Returns the SCSI status that was returned by the HBA or target device. If the status is not SUCCESS, the miniport driver should set the <b>SrbStatus</b> member to SRB_STATUS_ERROR.

`SenseInfoBuffer`

Points to the request-sense buffer. A miniport driver is not required to provide request-sense data after a CHECK CONDITION.

`SenseInfoBufferLength`

Indicates the size in bytes of the request-sense buffer. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred.

`SrbExtension`

Points to the Srb extension. A miniport driver must not use this member if it set <b>SrbExtensionSize</b> to zero in the SCSI_HW_INITIALIZATION_DATA. The memory at <b>SrbExtension</b> is not initialized by the OS-specific port driver, and the miniport driver-determined data can be accessed directly by the HBA. The corresponding physical address can be obtained by calling <a href="..\srb\nf-srb-scsiportgetphysicaladdress.md">ScsiPortGetPhysicalAddress</a> with the <b>SrbExtension</b> pointer.

`SrbFlags`

Indicates various parameters and options about the request. <b>SrbFlags</b> is read-only, except when SRB_FLAGS_UNSPECIFIED_DIRECTION is set and miniport drivers of subordinate DMA adapters are required to update SRB_FLAGS_DATA_IN or SRB_FLAGS_DATA_OUT. This member can have one or more of the following flags set:

`SrbStatus`

Returns the status of the completed request. This member should be set by the miniport driver before it notifies the OS-specific driver that the request has completed by calling <a href="..\srb\nf-srb-scsiportnotification.md">ScsiPortNotification</a> with <b>RequestComplete</b>. The value of this member can be one of the following:

`TargetId`

Indicates the target controller or device on the bus.

`TimeOutValue`

Indicates the interval in seconds that the request can execute before the OS-specific port driver might consider it timed out. Miniport drivers are not required to time requests because the port driver already does.

## Remarks
Windows storage class and filter drivers can send SRBs with the following <b>Function</b> values to the system port driver:
<ul>
<li>
SRB_FUNCTION_CLAIM_DEVICE to indicate that the class driver supports a peripheral identified in the SRB by the <b>PathId</b>, <b>TargetId</b>, and <b>Lun</b> members.

</li>
<li>
SRB_ATTACH_DEVICE to indicate that a filter driver, layered above a class driver, wants requests for a particular peripheral to be routed first to the filter driver.

</li>
<li>
SRB_FUNCTION_RELEASE_DEVICE to indicate that a class driver is releasing its claim on a particular peripheral.

</li>
<li>
SRB_FUNCTION_FLUSH_QUEUE to request cancellation of any requests currently queued in the port driver to a particular peripheral.

</li>
<li>
SRB_FUNCTION_RELEASE_QUEUE to request that the port driver release a frozen queue of requests to a particular peripheral.

</li>
</ul>The preceding SRB_FUNCTION_<i>XXX</i>  are never set in SRBs sent to SCSI miniport drivers. SRB_FUNCTION_REMOVE_DEVICE is defined for use in future versions of the system. It, too, is never set in SRBs sent to SCSI miniport drivers. SRB_FUNCTION_WMI_REQUEST is valid only in SCSI_WMI_REQUEST_BLOCK. A storage class or filter driver uses this to send WMI requests to the port driver.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | srb.h (include Srb.h) |

## See Also

<a href="..\ntddscsi\ns-ntddscsi-_srb_io_control.md">SRB_IO_CONTROL</a>

<a href="..\srb\nf-srb-scsiportgetsrb.md">ScsiPortGetSrb</a>

<a href="..\storport\ns-storport-_hw_initialization_data.md">HW_INITIALIZATION_DATA (SCSI)</a>

<a href="..\srb\nf-srb-scsiportgetphysicaladdress.md">ScsiPortGetPhysicalAddress</a>

<a href="..\srb\ns-srb-_port_configuration_information.md">PORT_CONFIGURATION_INFORMATION (SCSI)</a>

<a href="..\srb\nf-srb-scsiportiomaptransfer.md">ScsiPortIoMapTransfer</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff545387">ExInterlockedFreeToZone</a>

<a href="..\srb\nf-srb-scsiportnotification.md">ScsiPortNotification</a>

<a href="..\storport\ns-storport-_scsi_wmi_request_block.md">SCSI_WMI_REQUEST_BLOCK</a>

<a href="..\wdm\nf-wdm-exfreepool.md">ExFreePool</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SCSI_REQUEST_BLOCK structure%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>