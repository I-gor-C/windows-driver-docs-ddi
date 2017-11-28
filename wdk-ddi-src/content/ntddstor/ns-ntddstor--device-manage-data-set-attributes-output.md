---
UID: NS.ntddstor._DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT
title: DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT
author: windows-driver-content
description: The DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT structure describes output for IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES control code requests for some data set management actions.
old-location: storage\device_manage_data_set_attributes_output.htm
old-project: storage
ms.assetid: FFC52136-8A1C-48F6-A846-C1C5BFB4570C
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT, DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT, *PDEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT
req.alt-loc: ntddstor.h
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

# DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT structure



## -description
<p>The <b>DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT</b> structure describes output for  <a href="https://msdn.microsoft.com/library/windows/hardware/ff560573">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a> control code requests for some data set management actions. </p>


## -syntax

````
typedef struct _DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT {
  ULONG                             Size;
  DEVICE_DATA_MANAGEMENT_SET_ACTION Action;
  ULONG                             Flags;
  ULONG                             OperationStatus;
  ULONG                             ExtendedError;
  ULONG                             TargetDetailedError;
  ULONG                             ReservedStatus;
  ULONG                             OutputBlockOffset;
  ULONG                             OutputBlockLength;
} DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT, *PDEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this structure. This is set to <b>sizeof</b>(DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT).</p>
</dd>

### -field <b>Action</b>

<dd>
<p>The action related to the instance of this structure. This is a value from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552520">DEVICE_DATA_MANAGEMENT_SET_ACTION</a> enumeration.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags for the data set management action. See the <b>Flags</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560573">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a>.</p>
</dd>

### -field <b>OperationStatus</b>

<dd>
<p>An status resulting from the operation a performed for <b>Action</b>.</p>
</dd>

### -field <b>ExtendedError</b>

<dd>
<p>An extended error value originating from Windows or a driver.</p>
</dd>

### -field <b>TargetDetailedError</b>

<dd>
<p>An error value resulting from a failure execute the operation for <b>Action</b> at the target.</p>
</dd>

### -field <b>ReservedStatus</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>OutputBlockOffset</b>

<dd>
<p>The position, after the beginning of this structure, where action-specific data is located.</p>
</dd>

### -field <b>OutputBlockLength</b>

<dd>
<p>The length of the action-specific data.</p>
</dd>
</dl>

## -remarks
<p>Depending on the value of <b>Action</b>, an output block is written at an offset of <b>OutputBlockOffset</b> after the beginning of this structure. The size of the output block is specified in <b>OutputBlockLength</b>. </p>

<p>Currently, only the <b>DeviceDsmAction_Allocation</b> action uses this structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552520">DEVICE_DATA_MANAGEMENT_SET_ACTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439633">DEVICE_DATA_SET_LB_PROVISIONING_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560573">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
