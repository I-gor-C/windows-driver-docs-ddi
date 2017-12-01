---
UID: NF.storport.StorPortLogError
title: StorPortLogError
author: windows-driver-content
description: The StorPortLogError routine notifies the port driver that an error occurred.
old-location: storage\storportlogerror.htm
old-project: storage
ms.assetid: f653e6bf-e99b-4aa2-aa54-d7482d326720
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortLogError
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortLogError
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: StorPortDeprecated
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# StorPortLogError function



## -description
<p>The <b>StorPortLogError</b> routine notifies the port driver that an error occurred. </p>


## -syntax

````
STORPORT_API VOID StorPortLogError(
  _In_     PVOID               HwDeviceExtension,
  _In_opt_ PSCSI_REQUEST_BLOCK Srb,
  _In_     UCHAR               PathId,
  _In_     UCHAR               TargetId,
  _In_     UCHAR               Lun,
  _In_     ULONG               ErrorCode,
  _In_     ULONG               UniqueId
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport immediately after the miniport driver calls <a href="..\storport\nf-storport-storportinitialize.md">StorPortInitialize</a>. The port driver frees this memory when it removes the device. </p>
</dd>

### -param <i>Srb</i> [in, optional]

<dd>
<p>Pointer to a SCSI request block if one is associated with the error. Otherwise, this parameter is <b>NULL</b>. </p>
</dd>

### -param <i>PathId</i> [in]

<dd>
<p>Identifies the SCSI bus. </p>
</dd>

### -param <i>TargetId</i> [in]

<dd>
<p>Identifies the target controller or device on the bus. </p>
</dd>

### -param <i>Lun</i> [in]

<dd>
<p>Identifies the logical unit number of the target device. </p>
</dd>

### -param <i>ErrorCode</i> [in]

<dd>
<p>Specifies an error code indicating one of the following values as the type of error.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SP_BAD_FW_ERROR</p>
</td>
<td>
<p>Indicates the driver has detected bad or old firmware. The device will not be used.</p>
</td>
</tr>
<tr>
<td>
<p>SP_BAD_FW_WARNING</p>
</td>
<td>
<p>Indicates the driver has detected a card with old or bad firmware, which can result in reduced performance or functionality.</p>
</td>
</tr>
<tr>
<td>
<p>SP_BUS_PARITY_ERROR</p>
</td>
<td>
<p>Indicates a SCSI bus parity error was detected.</p>
</td>
</tr>
<tr>
<td>
<p>SP_BUS_TIME_OUT</p>
</td>
<td>
<p>Indicates a SCSI bus connection to a logical unit timed out.</p>
</td>
</tr>
<tr>
<td>
<p>SP_INTERNAL_ADAPTER_ERROR</p>
</td>
<td>
<p>Indicates an internal HBA error was detected.</p>
</td>
</tr>
<tr>
<td>
<p>SP_INVALID_RESELECTION</p>
</td>
<td>
<p>Indicates a logical unit reselected unexpectedly or with an invalid queue tag.</p>
</td>
</tr>
<tr>
<td>
<p>SP_IRQ_NOT_RESPONDING</p>
</td>
<td>
<p>Indicates the HBA is not interrupting when expected.</p>
</td>
</tr>
<tr>
<td>
<p>SP_PROTOCOL_ERROR</p>
</td>
<td>
<p>Indicates the miniport driver detected a SCSI bus protocol error.</p>
</td>
</tr>
<tr>
<td>
<p>SP_REQUEST_TIMEOUT</p>
</td>
<td>
<p>Indicates an operation to the controller has timed out.</p>
</td>
</tr>
<tr>
<td>
<p>SP_UNEXPECTED_DISCONNECT</p>
</td>
<td>
<p>Indicates that a target disconnected unexpectedly.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>UniqueId</i> [in]

<dd>
<p>Specifies a unique identifier for the error. This value differentiates the current error from other errors with the same <i>ErrorCode</i> value. For some miniport drivers, this identifies the line of code where the error was detected. For others, it is additional information returned by the HBA. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>The port driver will log an error to the system event log.</p>

<p>Starting in Windows 8, the <i>Srb</i> parameter may point to either <a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a> or <a href="..\srb\ns-srb--storage-request-block.md">STORAGE_REQUEST_BLOCK</a>. If the function identifier in the <b>Function</b> field of <i>Srb</i> is <b>SRB_FUNCTION_STORAGE_REQUEST_BLOCK</b>, the SRB is a <b>STORAGE_REQUEST_BLOCK</b> request structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.storport_storportdeprecated">StorPortDeprecated</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a>
</dt>
<dt>
<a href="..\srb\nf-srb-scsiportlogerror.md">ScsiPortLogError</a>
</dt>
<dt>
<a href="..\srb\ns-srb--storage-request-block.md">STORAGE_REQUEST_BLOCK</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportlogsystemevent.md">StorPortLogSystemEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortLogError routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
