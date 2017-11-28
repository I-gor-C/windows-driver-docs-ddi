---
UID: NS.ntifs._FSCTL_OFFLOAD_WRITE_INPUT
title: FSCTL_OFFLOAD_WRITE_INPUT
author: windows-driver-content
description: The FSCTL_OFFLOAD_WRITE_INPUT structure contains the input for the FSCTL_OFFLOAD_WRITE control code request.
old-location: ifsk\fsctl_offload_write_input.htm
old-project: ifsk
ms.assetid: 4ADBBBDC-02DD-4D1A-B697-6286D7513B2E
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FSCTL_OFFLOAD_WRITE_INPUT, FSCTL_OFFLOAD_WRITE_INPUT, *PFSCTL_OFFLOAD_WRITE_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FSCTL_OFFLOAD_WRITE_INPUT
req.alt-loc: ntifs.h
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

# FSCTL_OFFLOAD_WRITE_INPUT structure



## -description
<p>The <b>FSCTL_OFFLOAD_WRITE_INPUT</b> structure contains the input for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451122">FSCTL_OFFLOAD_WRITE</a> control code request.</p>


## -syntax

````
typedef struct _FSCTL_OFFLOAD_WRITE_INPUT {
  ULONG     Size;
  ULONG     Flags;
  ULONGLONG FileOffset;
  ULONGLONG CopyLength;
  ULONGLONG TransferOffset;
  UCHAR     Token[512];
} FSCTL_OFFLOAD_WRITE_INPUT, *PFSCTL_OFFLOAD_WRITE_INPUT;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this structure. Set this member to <b>sizeof</b>(FSCTL_OFFLOAD_WRITE_INPUT).</p>
</dd>

### -field <b>Flags</b>

<dd>
<p> This member is not used. Set to 0.</p>
</dd>

### -field <b>FileOffset</b>

<dd>
<p> The position in the file to begin writing to. The offset value must be aligned to a logical sector boundary on the volume.</p>
</dd>

### -field <b>CopyLength</b>

<dd>
<p> The length, in bytes, of data to write, starting at <b>FileOffset</b>. The length  value must align to a logical sector boundary on the volume, except when the length matches end-of-file.</p>
</dd>

### -field <b>TransferOffset</b>

<dd>
<p> The position in the data associated with <b>Token</b> to begin writing from.</p>
</dd>

### -field <b>Token</b>

<dd>
<p>A byte array that contains a token structure, <a href="https://msdn.microsoft.com/library/windows/hardware/hh451469">STORAGE_OFFLOAD_TOKEN</a>, representing a file data range to be logically written. The contents of <b>Token</b>  must remain unmodified between offload operations.</p>
</dd>
</dl>

## -remarks
<p><b>CopyLength</b> can be zero. The value of <b>FileOffset</b> + <b>CopyLength</b> is bounded by both <b>MAXULONGLONG</b> and <b>MAXFILESIZE</b>. <a href="https://msdn.microsoft.com/library/windows/hardware/hh451122">FSCTL_OFFLOAD_WRITE</a> will return with <b>STATUS_INVALID_PARAMETER</b> if these conditions are not met.</p>

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
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451101">FSCTL_OFFLOAD_READ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451122">FSCTL_OFFLOAD_WRITE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451130">FSCTL_OFFLOAD_WRITE_OUTPUT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451469">STORAGE_OFFLOAD_TOKEN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FSCTL_OFFLOAD_WRITE_INPUT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
