---
UID: NF.wdm.ClfsAdvanceLogBase
title: ClfsAdvanceLogBase
author: windows-driver-content
description: The ClfsAdvanceLogBase routine sets the base LSN of a CLFS stream.
old-location: kernel\clfsadvancelogbase.htm
old-project: kernel
ms.assetid: 00f776f7-83c5-4856-a1d3-8b76122d3986
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ClfsAdvanceLogBase
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsAdvanceLogBase
req.alt-loc: Clfs.sys,Ext-MS-Win-fs-clfs-l1-1-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Clfs.lib
req.dll: Clfs.sys
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ClfsAdvanceLogBase function



## -description
<p>The <b>ClfsAdvanceLogBase</b> routine sets the base LSN of a CLFS stream.</p>


## -syntax

````
NTSTATUS ClfsAdvanceLogBase(
  _Inout_ PVOID     pvMarshalContext,
  _In_    PCLFS_LSN plsnBase,
  _In_    ULONG     fFlags
);
````


## -parameters
<dl>

### -param pvMarshalContext [in, out]

<dd>
<p>A pointer to an opaque context that represents a marshalling area associated with a CLFS stream. The caller previously obtained this pointer by calling <a href="..\wdm\nf-wdm-clfscreatemarshallingarea.md">ClfsCreateMarshallingArea</a>.</p>
</dd>

### -param plsnBase [in]

<dd>
<p>A pointer to a <a href="kernel.clfs_lsn">CLFS_LSN</a> structure that contains the new base LSN. This parameter must be the LSN of one of the records in the stream. Also, this parameter must be greater than or equal to the stream's current base LSN and less than or equal to the stream's current last LSN.</p>
</dd>

### -param fFlags [in]

<dd>
<p>This parameter is reserved for system use. Callers must set this parameter to zero.</p>
</dd>
</dl>

## -returns
<p><b>ClfsAdvanceLogBase</b> returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h.</p>

## -remarks
<p><b>ClfsAdvanceLogBase</b> does not write any records to the CLFS log; the only updates to the log are in the metadata. If you want to update the base LSN and write a restart record to a stream at the same time, call <a href="..\wdm\nf-wdm-clfswriterestartarea.md">ClfsWriteRestartArea</a>.</p>

<p>Whenever possible, CLFS avoids writing queued log records that have LSNs less than the new base LSN to stable storage.</p>

<p><b>ClfsAdvanceLogBase</b> does not check to see whether the LSN supplied in <i>plsnBase</i> is actually the LSN of one of the records in the stream. If the caller sets <i>plsnBase</i> to an LSN that is not the LSN of one of the records in the stream, the stream's base LSN will be set to a meaningless value.</p>

<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.</p>
</td>
</tr>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-clfswriterestartarea.md">ClfsWriteRestartArea</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsAdvanceLogBase routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
