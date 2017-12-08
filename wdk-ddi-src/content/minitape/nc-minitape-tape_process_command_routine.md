---
UID: NC.minitape.TAPE_PROCESS_COMMAND_ROUTINE
title: TAPE_PROCESS_COMMAND_ROUTINE
author: windows-driver-content
description: TapeMiniCreatePartition handles the device-specific aspects of an IOCTL_TAPE_CREATE_PARTITION request. This routine is required.
old-location: storage\tapeminicreatepartition.htm
old-project: storage
ms.assetid: 6675d840-8b13-44ef-bbdb-84d683240175
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _PROCESSOR_NUMBER, PROCESSOR_NUMBER, *PPROCESSOR_NUMBER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: minitape.h
req.include-header: Minitape.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TapeMiniCreatePartition
req.alt-loc: minitape.h
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
---

# TAPE_PROCESS_COMMAND_ROUTINE callback



## -description
<i>TapeMiniCreatePartition</i> handles the device-specific aspects of an <a href="..\ntddtape\ni-ntddtape-ioctl_tape_create_partition.md">IOCTL_TAPE_CREATE_PARTITION</a> request. This routine is required.


## -prototype

````
TAPE_PROCESS_COMMAND_ROUTINE TapeMiniCreatePartition;

TAPE_STATUS TapeMiniCreatePartition(
  _Inout_  PVOID               MinitapeExtension,
  _Inout_  PVOID               CommandExtension,
  _Inout_  PVOID               CommandParameters,
  _Inout_  PSCSI_REQUEST_BLOCK Srb,
  _In_     ULONG               CallNumber,
  _In_opt_ TAPE_STATUS         StatusOfLastCommand,
  _Inout_  PULONG              RetryFlags
)
{ ... }
````


## -parameters

### -param MinitapeExtension [in, out]

Pointer to the driver-specific minitape extension. This is <b>NULL</b> if the miniclass driver did not request a minitape extension when it initialized.

### -param CommandExtension [in, out]

Pointer to the command extension. This is <b>NULL</b> if the miniclass driver did not request a command extension when it initialized.

### -param CommandParameters [in, out]

Pointer to a buffer allocated by the caller that contains a <a href="storage.tape_create_partition">TAPE_CREATE_PARTITION</a> structure.

### -param Srb [in, out]

Pointer to an SRB allocated and partially filled in by the tape class driver. <i>TapeMiniCreatePartition</i> must fill in the CDB in the SRB. <i>TapeMiniCreatePartition</i> might fill in other SRB members, depending on the requirements of its devices.

### -param CallNumber [in]

Specifies the number of times <i>TapeMiniCreatePartition</i> has been called to process a given tape command. <i>CallNumber</i> is zero the first time this routine is called and is incremented for each subsequent call until the miniclass driver returns a <a href="storage.tape_status">TAPE_STATUS</a> value that indicates the command is complete.

### -param StatusOfLastCommand [in, optional]

Specifies the status of the last command. In the first call to <i>TapeMiniCreatePartition</i> to process a given request, <i>StatusOfLastCommand </i>is TAPE_STATUS_SUCCESS. In subsequent calls, <i>StatusOfLastCommand </i>is either TAPE_STATUS_SUCCESS or an error status if an error occurred and the tape miniclass driver set RETURN_ERRORS in <i>RetryFlags</i> in the previous call. 

### -param RetryFlags [in, out]

Pointer to a variable that specifies what action the tape class driver should take when a tape device reports an error.
The low-order word specifies the number of retries to perform in the event of a SCSI command failure. The default is zero (no retries).
The high-order word contains flags that specify how the tape class driver should return control if an error occurs:
<ul>
<li>
If RETURN_ERRORS and IGNORE_ERRORS are clear (the default) the tape class driver returns a failure status to the original requester.
</li>
<li>
If the miniclass driver sets RETURN_ERRORS, the tape class driver calls <i>TapeMiniCreatePartition</i> with <i>StatusOfLastCommand</i> set to a failure status.
</li>
<li>
If the miniclass driver sets IGNORE_ERRORS, the tape class driver converts a failure status to success and calls <i>TapeMiniCreatePartition</i> with <i>StatusOfLastCommand </i>set to success.
</li>
</ul>

## -returns
<dl>
<dt><b>TAPE_STATUS_SEND_SRB_AND_CALLBACK</b></dt>
</dl>Indicates to the tape class driver that the SRB has been filled in and is ready to be sent to the target device. By default, the tape class driver calls <i>TapeMiniCreatePartition</i> again only if the SRB succeeds. A miniclass driver can modify the default behavior by setting <i>RetryFlags</i> before returning from <i>TapeMiniCreatePartition</i>.
<dl>
<dt><b>TAPE_STATUS_CALLBACK</b></dt>
</dl>Directs the tape class driver to increment <i>CallNumber</i> and call <i>TapeMiniCreatePartition</i> again without sending an SRB to the tape device. 
<dl>
<dt><b>TAPE_STATUS_CHECK_TEST_UNIT_READY</b></dt>
</dl>Directs the tape class driver to fill in an SRB for the TEST UNIT READY command and send the SRB to the device.
<dl>
<dt><b>TAPE_STATUS_<i>XXX</i></b></dt>
</dl>Any other return code indicates to the tape class driver that the command is complete and indicates success, failure, or warning. Possible completion return values for this routine include, but are not limited to:
<dl>
<dd>
TAPE_STATUS_SUCCESS
</dd>
<dd>
TAPE_STATUS_INSUFFICIENT_RESOURCES
</dd>
<dd>
TAPE_STATUS_INVALID_DEVICE_REQUEST
</dd>
<dd>
TAPE_STATUS_INVALID_PARAMETER
</dd>
<dd>
TAPE_STATUS_IO_DEVICE_ERROR
</dd>
<dd>
TAPE_STATUS_MEDIA_WRITE_PROTECTED
</dd>
<dd>
TAPE_STATUS_NOT_IMPLEMENTED
</dd>
</dl>TAPE_STATUS_SUCCESS

TAPE_STATUS_INSUFFICIENT_RESOURCES

TAPE_STATUS_INVALID_DEVICE_REQUEST

TAPE_STATUS_INVALID_PARAMETER

TAPE_STATUS_IO_DEVICE_ERROR

TAPE_STATUS_MEDIA_WRITE_PROTECTED

TAPE_STATUS_NOT_IMPLEMENTED

 

## -remarks
<i>TapeMiniCreatePartition</i> creates a partition on a tape by filling in the CDB in an SRB passed by the tape class driver. Creating a partition typically requires a series of SRBs to complete the operation. After <i>TapeMiniCreatePartition</i> fills in a given SRB and returns, the tape class driver sends the SRB to the target device and, depending on the result of the SRB and the value of <i>RetryFlags</i>, calls <i>TapeMiniCreatePartition</i> again.

<i>TapeMiniCreatePartition</i> must fill in the following members in the SRB before returning to the tape class driver:

<b>Cdb</b> - Pointer to the SCSI CDB for the command. Clear the CDB with <b>TapeClassZeroMemory</b> before filling it in.

<b>CdbLength</b> - Specifies the number of bytes in the CDB.

<i>TapeMiniCreatePartition</i> might also fill in the following members in the SRB:

<b>DataBuffer</b> - Pointer to the data buffer to be transferred. Use <a href="storage.tapeclassallocatesrbbuffer">TapeClassAllocateSrbBuffer</a> to allocate a <b>DataBuffer</b> of length greater than or equal to <b>DataTransferLength</b>.

<b>DataTransferLength</b> - Specifies the number of bytes to be transferred in the SRB. This member is set by <b>TapeClassAllocateSrbBuffer</b>.

<b>TimeOutValue</b> - Specifies a time-out value for this command, overriding the default time-out value from the tape class driver's device extension.

<b>SrbFlags</b> - Specifies a flag for this command. The tape miniclass driver must set SRB_FLAGS_DATA_OUT if the SRB is sending data to the tape drive. This member can be zero if the SRB is requesting data from the tape drive or if no data is being transferred by the command.

If the tape miniclass driver stores partition information in the minitape extension, <i>TapeMiniCreatePartition</i> updates the extension before returning to the tape class driver with TAPE_STATUS_SUCCESS.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Minitape.h (include Minitape.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.scsi_request_block">SCSI_REQUEST_BLOCK</a>
</dt>
<dt>
<a href="storage.tapeclassallocatesrbbuffer">TapeClassAllocateSrbBuffer</a>
</dt>
<dt>
<a href="storage.tapeclasszeromemory">TapeClassZeroMemory</a>
</dt>
<dt>
<a href="storage.tape_status">TAPE_STATUS</a>
</dt>
<dt>
<a href="..\ntddtape\ni-ntddtape-ioctl_tape_create_partition.md">IOCTL_TAPE_CREATE_PARTITION</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TapeMiniCreatePartition routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
