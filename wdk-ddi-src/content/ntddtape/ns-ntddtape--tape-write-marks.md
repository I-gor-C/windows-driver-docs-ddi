---
UID: NS.ntddtape._TAPE_WRITE_MARKS
title: TAPE_WRITE_MARKS
author: windows-driver-content
description: The TAPE_WRITE_MARKS structure is used in conjunction with an IOCTL_TAPE_WRITE_MARKS request to write a setmark, a filemark, a short filemark, or a long filemark to tape.
old-location: storage\tape_write_marks.htm
old-project: storage
ms.assetid: 5baa7fd0-e806-4da8-9c87-c86ebc003e60
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: TAPE_WRITE_MARKS, TAPE_WRITE_MARKS, *PTAPE_WRITE_MARKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddtape.h
req.include-header: Ntddtape.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TAPE_WRITE_MARKS
req.alt-loc: ntddtape.h
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

# TAPE_WRITE_MARKS structure



## -description
<p>The TAPE_WRITE_MARKS structure is used in conjunction with an <a href="..\ntddtape\ni-ntddtape-ioctl-tape-write-marks.md">IOCTL_TAPE_WRITE_MARKS</a> request to write a setmark, a filemark, a short filemark, or a long filemark to tape. </p>


## -syntax

````
typedef struct _TAPE_WRITE_MARKS {
  ULONG   Type;
  ULONG   Count;
  BOOLEAN Immediate;
} TAPE_WRITE_MARKS, *PTAPE_WRITE_MARKS;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Indicates the type of mark to write. This member can have one of the following values: </p>
<table>
<tr>
<th>Type</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>TAPE_SETMARKS</p>
</td>
<td>
<p>Writes the number of setmarks specified by <b>Count</b>.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_FILEMARKS</p>
</td>
<td>
<p>Writes the number of filemarks specified by the <b>Count</b> parameter.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_SHORT_FILEMARKS</p>
</td>
<td>
<p>Writes the number of short filemarks specified by <b>Count</b>.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_LONG_FILEMARKS </p>
</td>
<td>
<p>Writes the number of long filemarks specified by <b>Count</b>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Count</b>

<dd>
<p>Indicates the number of marks to write. </p>
</dd>

### -field <b>Immediate</b>

<dd>
<p>When set to <b>TRUE</b>, indicates that the target device should return status immediately. When set to <b>FALSE</b>, indicates that the device should return status after the operation is complete.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddtape.h (include Ntddtape.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddtape\ni-ntddtape-ioctl-tape-write-marks.md">IOCTL_TAPE_WRITE_MARKS</a>
</dt>
<dt>
<a href="storage.tapeminiwritemarks">TapeMiniWriteMarks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TAPE_WRITE_MARKS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
