---
UID: NF.ntifs.IsReparseTagMicrosoft
title: IsReparseTagMicrosoft
author: windows-driver-content
description: The IsReparseTagMicrosoft macro determines whether a reparse point tag indicates a Microsoft reparse point.
old-location: ifsk\isreparsetagmicrosoft.htm
old-project: ifsk
ms.assetid: 9c5abef5-36ff-4f10-8e4e-b8d36d995246
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IsReparseTagMicrosoft
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IsReparseTagMicrosoft
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
req.irql: Any level
req.iface: 
---

# IsReparseTagMicrosoft function



## -description
<p>The <b>IsReparseTagMicrosoft</b> macro determines whether a reparse point tag indicates a Microsoft reparse point. </p>


## -syntax

````
ULONG IsReparseTagMicrosoft(
  _In_ ULONG _tag
);
````


## -parameters
<dl>

### -param _tag [in]

<dd>
<p>Reparse point tag to be tested. </p>
</dd>
</dl>

## -returns
<p>If the tag is a Microsoft tag, the return value is nonzero. If the tag is a non-Microsoft tag, the return value is zero. </p>

## -remarks
<p>Only Microsoft reparse points can use Microsoft tags. Third-party reparse points must use non-Microsoft tags. However, third-party drivers can set Microsoft reparse points. For more information, see the Remarks section of the reference entry for the <a href="..\ntifs\ns-ntifs--reparse-guid-data-buffer.md">REPARSE_GUID_DATA_BUFFER</a> structure. </p>

<p>For more information about reparse points, see the Microsoft Windows SDK documentation. </p>

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
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltfscontrolfile.md">FltFsControlFile</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-flttagfile.md">FltTagFile</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltuntagfile.md">FltUntagFile</a>
</dt>
<dt>
<a href="ifsk.fsctl_delete_reparse_point">FSCTL_DELETE_REPARSE_POINT</a>
</dt>
<dt>
<a href="ifsk.fsctl_get_reparse_point">FSCTL_GET_REPARSE_POINT</a>
</dt>
<dt>
<a href="ifsk.fsctl_set_reparse_point">FSCTL_SET_REPARSE_POINT</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-isreparsetagnamesurrogate.md">IsReparseTagNameSurrogate</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--reparse-data-buffer.md">REPARSE_DATA_BUFFER</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--reparse-guid-data-buffer.md">REPARSE_GUID_DATA_BUFFER</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwfscontrolfile.md">ZwFsControlFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IsReparseTagMicrosoft function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
