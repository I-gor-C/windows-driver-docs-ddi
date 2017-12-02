---
UID: NF.srb.ScsiPortLogError
title: ScsiPortLogError
author: windows-driver-content
description: The ScsiPortLogError routine logs errors to the system event log when a miniport driver or its HBA detects a SCSI error condition.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
old-location: storage\scsiportlogerror.htm
old-project: storage
ms.assetid: 278f4fff-6e71-4544-8838-90f659c5029e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ScsiPortLogError
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: srb.h
req.include-header: Miniport.h, Scsi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ScsiPortLogError
req.alt-loc: Scsiport.lib,Scsiport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Scsiport.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# ScsiPortLogError function



## -description
<p>The <b>ScsiPortLogError</b> routine logs errors to the system event log when a miniport driver or its HBA detects a SCSI error condition.</p>


## -syntax

````
VOID ScsiPortLogError(
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

### -param HwDeviceExtension [in]

<dd>
<p>Pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the HBA's mapped access ranges. This area is available to the miniport driver in the <b>DeviceExtension-&gt;HwDeviceExtension</b> member of the HBA's device object immediately after the miniport driver calls <a href="..\srb\nf-srb-scsiportinitialize.md">ScsiPortInitialize</a>. The port driver frees this memory when it removes the device. </p>
</dd>

### -param Srb [in, optional]

<dd>
<p>Pointer to a SCSI request block if one is associated with the error. Otherwise, this parameter is <b>NULL</b>.</p>
</dd>

### -param PathId [in]

<dd>
<p>Identifies the SCSI bus.</p>
</dd>

### -param TargetId [in]

<dd>
<p>Identifies the target controller or device on the bus.</p>
</dd>

### -param Lun [in]

<dd>
<p>Identifies the logical unit number of the target device.</p>
</dd>

### -param ErrorCode [in]

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

### -param UniqueId [in]

<dd>
<p>Specifies a unique identifier for the error. This value differentiates the current error from other errors with the same <i>ErrorCode</i>. For some miniport drivers, this identifies the line of code where the error was detected. For others, it is additional information returned by the HBA.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A miniport driver should log all real hardware errors. However, it should not log common operational errors, such as selection time-outs or bus resets.</p>

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
<dt>Srb.h (include Miniport.h or Scsi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Scsiport.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\srb\nf-srb-scsiportnotification.md">ScsiPortNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ScsiPortLogError routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
