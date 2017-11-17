---
UID: NS.ntddstor._DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS
title: DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS
author: windows-driver-content
description: The DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS structure specifies the parameters for an offload write action related to the data-set attributes for a device.
old-location: storage\device_dsm_offload_write_parameters.htm
ms.assetid: B0E9DABD-0D5B-4F5D-8CB0-470AC126F9C0
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS
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
ms.keywords: DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS, DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS, *PDEVICE_DSM_OFFLOAD_WRITE_PARAMETERS
req.iface: 
---

# DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS structure



## -description
<p>The <b>DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS</b> structure specifies the parameters for an offload write action related to the data-set attributes for a device. </p>
<p>This parameter structure is used in an offload write  action for an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560573">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a> request.  The <b>Action</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552527">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a> structure is set to <b>DeviceDsmAction_OffloadWrite</b>, and <b>ParameterBlockOffset</b> indicates the location of <b>DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS</b>.</p>


## -syntax

````
typedef struct _DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS {
  ULONG                 Flags;
  ULONG                 Reserved;
  ULONGLONG             TokenOffset;
  STORAGE_OFFLOAD_TOKEN Token;
} DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS, *PDEVICE_DSM_OFFLOAD_WRITE_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>Not used.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>TokenOffset</b>

<dd>
<p>The offset, in bytes, within the data block specified by <b>Token</b> to begin writing from.</p>
</dd>

### -field <b>Token</b>

<dd>
<p>The unique identifier of the data block to write from.</p>
</dd>
</dl>

## -remarks
<p>The <b>ParameterBlockOffset</b> and <b>ParameterBlockLength</b> members  of <a href="https://msdn.microsoft.com/library/windows/hardware/ff552527">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a> are set to the location and length of the  <b>DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS</b> structure in the system buffer of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560573">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a> request.</p>

<p>The <b>DataSetRangesOffset</b> and <b>DataSetRangesLength</b> members of <a href="https://msdn.microsoft.com/library/windows/hardware/ff552527">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a> specify the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552523">DEVICE_DATA_SET_RANGE</a> structures for the extents of the offload write.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 8 and later versions of Windows.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552527">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560573">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
