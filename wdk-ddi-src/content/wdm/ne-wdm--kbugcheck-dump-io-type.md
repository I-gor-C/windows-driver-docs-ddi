---
UID: NE.wdm._KBUGCHECK_DUMP_IO_TYPE
title: KBUGCHECK_DUMP_IO_TYPE
author: windows-driver-content
description: The KBUGCHECK_DUMP_IO_TYPE enumeration type identifies the type of a section of data within a crash dump file.
old-location: kernel\kbugcheck_dump_io_type.htm
old-project: kernel
ms.assetid: 928be338-a588-4535-8395-229ec6f3ecb7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available on Microsoft Windows XP with Service Pack 1 (SP1), Windows Server 2003, and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KBUGCHECK_DUMP_IO_TYPE
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# KBUGCHECK_DUMP_IO_TYPE enumeration



## -description
<p>The <b>KBUGCHECK_DUMP_IO_TYPE</b> enumeration type identifies the type of a section of data within a crash dump file.</p>


## -syntax

````
typedef enum _KBUGCHECK_DUMP_IO_TYPE { 
  KbDumpIoInvalid        = 0,
  KbDumpIoHeader         = 1,
  KbDumpIoBody           = 2,
  KbDumpIoSecondaryData  = 3,
  KbDumpIoComplete       = 4
} KBUGCHECK_DUMP_IO_TYPE;
````


## -enum-fields
<dl>

### -field KbDumpIoInvalid

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>

### -field KbDumpIoHeader

<dd>
<p>Specifies that crash dump data is header information.</p>
</dd>

### -field KbDumpIoBody

<dd>
<p>Specifies that the crash dump data is part of the main body of the crash dump, such as the memory state at the time of the bug check.</p>
</dd>

### -field KbDumpIoSecondaryData

<dd>
<p>Specifies that the crash dump data is data returned by a <a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckSecondaryDumpDataCallback</a> routine.</p>
</dd>

### -field KbDumpIoComplete

<dd>
<p>Specifies that the crash dump data has been completely written.</p>
</dd>
</dl>

## -remarks
<p><b>KBUGCHECK_DUMP_IO_TYPE</b> values are used in the <b>Type</b> member of <a href="..\wdm\ns-wdm--kbugcheck-dump-io.md">KBUGCHECK_DUMP_IO</a> to specify the type of data in an I/O operation on the crash dump file.</p>

<p>For more information about how this enumeration type is used, see <a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckDumpIoCallback</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available on Microsoft Windows XP with Service Pack 1 (SP1), Windows Server 2003, and later versions of the Windows operating system.</p>
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
<a href="..\wdm\ns-wdm--kbugcheck-dump-io.md">KBUGCHECK_DUMP_IO</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckDumpIoCallback</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckSecondaryDumpDataCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KBUGCHECK_DUMP_IO_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
