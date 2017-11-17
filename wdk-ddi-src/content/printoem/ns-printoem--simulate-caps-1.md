---
UID: NS.printoem._SIMULATE_CAPS_1
title: SIMULATE_CAPS_1
author: windows-driver-content
description: The SIMULATE_CAPS_1 structure contains information about the types of simulations a spooler supports.
old-location: print\simulate_caps_1.htm
ms.assetid: 17f5d8bf-a3e7-4ff5-9019-24c66875b786
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SIMULATE_CAPS_1
req.alt-loc: printoem.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: SIMULATE_CAPS_1, SIMULATE_CAPS_1, *PSIMULATE_CAPS_1
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# SIMULATE_CAPS_1 structure



## -description
<p>The SIMULATE_CAPS_1 structure contains information about the types of simulations a spooler supports.</p>


## -syntax

````
typedef struct _SIMULATE_CAPS_1 {
  DWORD dwLevel;
  DWORD dwPageOrderFlags;
  DWORD dwNumberOfCopies;
  DWORD dwCollate;
  DWORD dwNupOptions;
} SIMULATE_CAPS_1, *PSIMULATE_CAPS_1;
````


## -struct-fields
<dl>

### -field <b>dwLevel</b>

<dd>
<p>Specifies the version of this structure. This value must be 1.</p>
</dd>

### -field <b>dwPageOrderFlags</b>

<dd>
<p>Specifies the order in which pages will be printed. This member can be set to one of the following values:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>BOOKLET_PRINT</p>
</td>
<td>
<p>Pages should be printed in booklet form, with two document pages printed on one side of a physical page. In landscape mode, the two document pages are printed side-by-side on the paper. In portrait mode, the two document pages are printed top-and-bottom.</p>
</td>
</tr>
<tr>
<td>
<p>NORMAL_PRINT</p>
</td>
<td>
<p>Pages should be printed in normal order: page 1, page 2, and so on.</p>
</td>
</tr>
<tr>
<td>
<p>REVERSE_PRINT</p>
</td>
<td>
<p>Pages should be printed in reverse order: last page, next-to-last page, and so on.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwNumberOfCopies</b>

<dd>
<p>Specifies the maximum number of copies the spooler can handle.</p>
</dd>

### -field <b>dwCollate</b>

<dd>
<p>Specifies whether the spooler supports collation. A value of 1 indicates that the spooler supports collation, and a value of 0 indicates that it does not.</p>
</dd>

### -field <b>dwNupOptions</b>

<dd>
<p>Is a bitmask representing the various numbers of document pages the printer can print on a physical page. The least significant bit represents 1 document page per page, the next bit represents 2 document pages per page, the next bit represents 3 document pages per physical page, and so on. For example, 0x0000810B indicates that the spooler supports 1, 2, 4, 9, and 16 document pages per physical page.</p>
</dd>
</dl>

## -remarks
<p>The <b>IPrintCoreUI2::QuerySimulationSupport</b> method uses this structure to report the spooler's level of simulation support to a user-interface plug-in.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553074">IPrintCoreUI2::QuerySimulationSupport</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20SIMULATE_CAPS_1 structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
