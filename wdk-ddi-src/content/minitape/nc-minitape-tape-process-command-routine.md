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
ms.keywords: PROCESSOR_NUMBER, PROCESSOR_NUMBER, *PPROCESSOR_NUMBER
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
req.iface: 
---

# TAPE_PROCESS_COMMAND_ROUTINE callback



## -description
<p><i>TapeMiniCreatePartition</i> handles the device-specific aspects of an <a href="..\ntddtape\ni-ntddtape-ioctl-tape-create-partition.md">IOCTL_TAPE_CREATE_PARTITION</a> request. This routine is required.</p>


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
<dl>

### -param <i>MinitapeExtension</i> [in, out]

<dd>
<p>Pointer to the driver-specific minitape extension. This is <b>NULL</b> if the miniclass driver did not request a minitape extension when it initialized.</p>
</dd>

### -param <i>CommandExtension</i> [in, out]

<dd>
<p>Pointer to the command extension. This is <b>NULL</b> if the miniclass driver did not request a command extension when it initialized.</p>
</dd>

### -param <i>CommandParameters</i> [in, out]

<dd>
<p>Pointer to a buffer allocated by the caller that contains a <a href="..\ntddtape\ns-ntddtape--tape-create-partition.md">TAPE_CREATE_PARTITION</a> structure.</p>
</dd>

### -param <i>Srb</i> [in, out]

<dd>
<p>Pointer to an SRB allocated and partially filled in by the tape class driver. <i>TapeMiniCreatePartition</i> must fill in the CDB in the SRB. <i>TapeMiniCreatePartition</i> might fill in other SRB members, depending on the requirements of its devices.</p>
</dd>

### -param <i>CallNumber</i> [in]

<dd>
<p>Specifies the number of times <i>TapeMiniCreatePartition</i> has been called to process a given tape command. <i>CallNumber</i> is zero the first time this routine is called and is incremented for each subsequent call until the miniclass driver returns a <a href="..\minitape\ne-minitape--tape-status.md">TAPE_STATUS</a> value that indicates the command is complete.</p>
</dd>

### -param <i>StatusOfLastCommand</i> [in, optional]

<dd>
<p>Specifies the status of the last command. In the first call to <i>TapeMiniCreatePartition</i> to process a given request, <i>StatusOfLastCommand </i>is TAPE_STATUS_SUCCESS. In subsequent calls, <i>StatusOfLastCommand </i>is either TAPE_STATUS_SUCCESS or an error status if an error occurred and the tape miniclass driver set RETURN_ERRORS in <i>RetryFlags</i> in the previous call. </p>
</dd>

### -param <i>RetryFlags</i> [in, out]

<dd>
<p>Pointer to a variable that specifies what action the tape class driver should take when a tape device reports an error.</p>
<p>The low-order word specifies the number of retries to perform in the event of a SCSI command failure. The default is zero (no retries).</p>
<p>The high-order word contains flags that specify how the tape class driver should return control if an error occurs:</p>
<ul>
<li>
<p>If RETURN_ERRORS and IGNORE_ERRORS are clear (the default) the tape class driver returns a failure status to the original requester.</p>
</li>
<li>
<p>If the miniclass driver sets RETURN_ERRORS, the tape class driver calls <i>TapeMiniCreatePartition</i> with <i>StatusOfLastCommand</i> set to a failure status.</p>
</li>
<li>
<p>If the miniclass driver sets IGNORE_ERRORS, the tape class driver converts a failure status to success and calls <i>TapeMiniCreatePartition</i> with <i>StatusOfLastCommand </i>set to success.</p>
</li>
</ul>
</dd>
</dl>

## -returns
<dl>
<dt><b>TAPE_STATUS_SEND_SRB_AND_CALLBACK</b></dt>
</dl><p>Indicates to the tape class driver that the SRB has been filled in and is ready to be sent to the target device. By default, the tape class driver calls <i>TapeMiniCreatePartition</i> again only if the SRB succeeds. A miniclass driver can modify the default behavior by setting <i>RetryFlags</i> before returning from <i>TapeMiniCreatePartition</i>.</p><dl>
<dt><b>TAPE_STATUS_CALLBACK</b></dt>
</dl><p>Directs the tape class driver to increment <i>CallNumber</i> and call <i>TapeMiniCreatePartition</i> again without sending an SRB to the tape device. </p><dl>
<dt><b>TAPE_STATUS_CHECK_TEST_UNIT_READY</b></dt>
</dl><p>Directs the tape class driver to fill in an SRB for the TEST UNIT READY command and send the SRB to the device.</p><dl>
<dt><b>TAPE_STATUS_<i>XXX</i></b></dt>
</dl><p>Any other return code indicates to the tape class driver that the command is complete and indicates success, failure, or warning. Possible completion return values for this routine include, but are not limited to:</p><dl>
<dd>
<p>TAPE_STATUS_SUCCESS</p>
</dd>
<dd>
<p>TAPE_STATUS_INSUFFICIENT_RESOURCES</p>
</dd>
<dd>
<p>TAPE_STATUS_INVALID_DEVICE_REQUEST</p>
</dd>
<dd>
<p>TAPE_STATUS_INVALID_PARAMETER</p>
</dd>
<dd>
<p>TAPE_STATUS_IO_DEVICE_ERROR</p>
</dd>
<dd>
<p>TAPE_STATUS_MEDIA_WRITE_PROTECTED</p>
</dd>
<dd>
<p>TAPE_STATUS_NOT_IMPLEMENTED</p>
</dd>
</dl><p>TAPE_STATUS_SUCCESS</p>

<p>TAPE_STATUS_INSUFFICIENT_RESOURCES</p>

<p>TAPE_STATUS_INVALID_DEVICE_REQUEST</p>

<p>TAPE_STATUS_INVALID_PARAMETER</p>

<p>TAPE_STATUS_IO_DEVICE_ERROR</p>

<p>TAPE_STATUS_MEDIA_WRITE_PROTECTED</p>

<p>TAPE_STATUS_NOT_IMPLEMENTED</p>

<p> </p>

## -remarks
<p><i>TapeMiniCreatePartition</i> creates a partition on a tape by filling in the CDB in an SRB passed by the tape class driver. Creating a partition typically requires a series of SRBs to complete the operation. After <i>TapeMiniCreatePartition</i> fills in a given SRB and returns, the tape class driver sends the SRB to the target device and, depending on the result of the SRB and the value of <i>RetryFlags</i>, calls <i>TapeMiniCreatePartition</i> again.</p>

<p><i>TapeMiniCreatePartition</i> must fill in the following members in the SRB before returning to the tape class driver:</p>

<p><b>Cdb</b> - Pointer to the SCSI CDB for the command. Clear the CDB with <b>TapeClassZeroMemory</b> before filling it in.</p>

<p><b>CdbLength</b> - Specifies the number of bytes in the CDB.</p>

<p><i>TapeMiniCreatePartition</i> might also fill in the following members in the SRB:</p>

<p><b>DataBuffer</b> - Pointer to the data buffer to be transferred. Use <a href="..\minitape\nf-minitape-tapeclassallocatesrbbuffer.md">TapeClassAllocateSrbBuffer</a> to allocate a <b>DataBuffer</b> of length greater than or equal to <b>DataTransferLength</b>.</p>

<p><b>DataTransferLength</b> - Specifies the number of bytes to be transferred in the SRB. This member is set by <b>TapeClassAllocateSrbBuffer</b>.</p>

<p><b>TimeOutValue</b> - Specifies a time-out value for this command, overriding the default time-out value from the tape class driver's device extension.</p>

<p><b>SrbFlags</b> - Specifies a flag for this command. The tape miniclass driver must set SRB_FLAGS_DATA_OUT if the SRB is sending data to the tape drive. This member can be zero if the SRB is requesting data from the tape drive or if no data is being transferred by the command.</p>

<p>If the tape miniclass driver stores partition information in the minitape extension, <i>TapeMiniCreatePartition</i> updates the extension before returning to the tape class driver with TAPE_STATUS_SUCCESS.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a>
</dt>
<dt>
<a href="..\minitape\nf-minitape-tapeclassallocatesrbbuffer.md">TapeClassAllocateSrbBuffer</a>
</dt>
<dt>
<a href="..\minitape\nf-minitape-tapeclasszeromemory.md">TapeClassZeroMemory</a>
</dt>
<dt>
<a href="..\minitape\ne-minitape--tape-status.md">TAPE_STATUS</a>
</dt>
<dt>
<a href="..\ntddtape\ni-ntddtape-ioctl-tape-create-partition.md">IOCTL_TAPE_CREATE_PARTITION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TapeMiniCreatePartition routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
