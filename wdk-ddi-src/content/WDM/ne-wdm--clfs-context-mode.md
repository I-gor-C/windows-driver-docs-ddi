---
UID: NE.wdm._CLFS_CONTEXT_MODE
title: CLFS_CONTEXT_MODE
author: windows-driver-content
description: The CLFS_CONTEXT_MODE enumeration indicates the type of sequence that the Common Log File System (CLFS) driver follows when it reads a set of records from a stream.
old-location: kernel\clfs_context_mode.htm
ms.assetid: 35f2b42d-d67f-4fd4-adde-918a2587980b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CLFS_CONTEXT_MODE
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
req.iface: 
req.product: Windows 10 or later.
---

# CLFS_CONTEXT_MODE enumeration



## -description
<p>The <b>CLFS_CONTEXT_MODE</b> enumeration indicates the type of sequence that the Common Log File System (CLFS) driver follows when it reads a set of records from a stream.</p>


## -syntax

````
typedef enum _CLFS_CONTEXT_MODE { 
  ClfsContextNone      = 0,
  ClfsContextUndoNext  = 1,
  ClfsContextPrevious  = 2,
  ClfsContextForward   = 3
} CLFS_CONTEXT_MODE, *PCLFS_CONTEXT_MODE, **PPCLFS_CONTEXT_MODE;
````


## -enum-fields
<dl>

### -field <a id="ClfsContextNone"></a><a id="clfscontextnone"></a><a id="CLFSCONTEXTNONE"></a><b>ClfsContextNone</b>

<dd>
<p>Indicates that a variable of type <b>CLFS_CONTEXT_MODE</b> has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="ClfsContextUndoNext"></a><a id="clfscontextundonext"></a><a id="CLFSCONTEXTUNDONEXT"></a><b>ClfsContextUndoNext</b>

<dd>
<p>Indicates that the next record in the sequence is pointed to by the <a href="https://msdn.microsoft.com/4637fa0c-2f19-4f0c-bf13-f4ccac2e7284">undo-next LSN</a> of the current record.</p>
</dd>

### -field <a id="ClfsContextPrevious"></a><a id="clfscontextprevious"></a><a id="CLFSCONTEXTPREVIOUS"></a><b>ClfsContextPrevious</b>

<dd>
<p>Indicates that the next record in the sequence is pointed to by the <a href="https://msdn.microsoft.com/4637fa0c-2f19-4f0c-bf13-f4ccac2e7284">previous LSN</a> of the current record.</p>
</dd>

### -field <a id="ClfsContextForward"></a><a id="clfscontextforward"></a><a id="CLFSCONTEXTFORWARD"></a><b>ClfsContextForward</b>

<dd>
<p>Indicates that the next record in the sequence is the record in the stream that immediately follows the current record.</p>
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
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541682">ClfsReadLogRecord</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541690">ClfsReadNextLogRecord</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541709">ClfsReadRestartArea</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541699">ClfsReadPreviousRestartArea</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CLFS_CONTEXT_MODE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
