---
UID: NS.wdm._KBUGCHECK_DUMP_IO
title: KBUGCHECK_DUMP_IO
author: windows-driver-content
description: The KBUGCHECK_DUMP_IO structure describes an I/O operation on the crash dump file.
old-location: kernel\kbugcheck_dump_io.htm
old-project: kernel
ms.assetid: d1c246bd-314d-475f-9df8-f1bf90355a5a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KBUGCHECK_DUMP_IO, KBUGCHECK_DUMP_IO, *PKBUGCHECK_DUMP_IO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available on Microsoft Windows XP with Service Pack 1 (SP1), Windows Server 2003, and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KBUGCHECK_DUMP_IO
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# KBUGCHECK_DUMP_IO structure



## -description
<p>The <b>KBUGCHECK_DUMP_IO</b> structure describes an I/O operation on the crash dump file.</p>


## -syntax

````
typedef struct _KBUGCHECK_DUMP_IO {
  ULONG64                Offset;
  PVOID                  Buffer;
  ULONG                  BufferLength;
  KBUGCHECK_DUMP_IO_TYPE Type;
} KBUGCHECK_DUMP_IO, *PKBUGCHECK_DUMP_IO;
````


## -struct-fields
<dl>

### -field <b>Offset</b>

<dd>
<p>Specifies the current offset in the crash dump file, or -1 if the crash dump file is being written sequentially.</p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>Pointer to a buffer that contains the current data to be written to the dump file.</p>
</dd>

### -field <b>BufferLength</b>

<dd>
<p>Specifies the length of the buffer, in bytes, that is specified by the <b>Buffer</b> member.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>Specifies the <a href="..\wdm\ne-wdm--kbugcheck-dump-io-type.md">KBUGCHECK_DUMP_IO_TYPE</a> value that signifies the type of data to be written to the dump file.</p>
</dd>
</dl>

## -remarks
<p>For information about how this structure is used, see <a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckDumpIoCallback</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available on Microsoft Windows XP with Service Pack 1 (SP1), Windows Server 2003, and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ne-wdm--kbugcheck-dump-io-type.md">KBUGCHECK_DUMP_IO_TYPE</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckDumpIoCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KBUGCHECK_DUMP_IO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
