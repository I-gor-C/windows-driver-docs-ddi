---
UID: NF.rxce.RxCeBuildVC
title: RxCeBuildVC
author: windows-driver-content
description: RxCeBuildVC adds a virtual circuit to a specified RDBSS connection..
old-location: ifsk\rxcebuildvc.htm
old-project: ifsk
ms.assetid: b060bd22-113f-4f78-8763-d1d19cf198b8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxCeBuildVC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxce.h
req.include-header: Rxce.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxCeBuildVC
req.alt-loc: rxce.h
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
req.iface: 
req.product: Windows 10 or later.
---

# RxCeBuildVC function



## -description
<p><b>RxCeBuildVC</b> adds a virtual circuit to a specified RDBSS connection..</p>


## -syntax

````
NTSTATUS RxCeBuildVC(
  _Inout_ PRXCE_VC         pVc,
  _In_    PRXCE_CONNECTION pConnection
);
````


## -parameters
<dl>

### -param <i>pVc</i> [in, out]

<dd>
<p>On input, this parameter contains a pointer to a handle for an uninitialized virtual circuit. On output when this call is successful, the virtual circuit is associated with the specified connection and the state of the virtual circuit is initialized as active.</p>
</dd>

### -param <i>pConnection</i> [in]

<dd>
<p>A pointer to the connection on which the virtual circuit is to be added.</p>
</dd>
</dl>

## -returns
<p><b>RxCeBuildVC</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The allocation of nonpaged pool memory needed by this routine failed. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameters passed to this routine was invalid. </p>

<p> </p>

## -remarks
<p>When <b>RxCeBuildVC</b> is successful, the data members in the RXCE_VC structure pointed to by the <i>pVC</i> parameter will be properly initialized and the virtual circuit will be added to the specified RDBSS connection. </p>

<p>When <b>RxCeBuildVC</b> is successful, the data members in the RXCE_VC structure pointed to by the <i>pVC</i> parameter will be properly initialized and the virtual circuit will be added to the specified RDBSS connection. </p>

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
<dt>Rxce.h (include Rxce.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554332">RxCeTearDownVC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeBuildVC function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
