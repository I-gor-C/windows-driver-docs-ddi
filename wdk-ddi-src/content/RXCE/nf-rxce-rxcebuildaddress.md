---
UID: NF.rxce.RxCeBuildAddress
title: RxCeBuildAddress
author: windows-driver-content
description: RxCeBuildAddress associates a transport address with a transport binding.
old-location: ifsk\rxcebuildaddress.htm
ms.assetid: e8845b15-4427-45ea-9192-352d82c89c6a
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: rxce.h
req.include-header: Rxce.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxCeBuildAddress
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
ms.keywords: RxCeBuildAddress
req.iface: 
req.product: Windows 10 or later.
---

# RxCeBuildAddress function



## -description
<p><b>RxCeBuildAddress</b> associates a transport address with a transport binding.</p>


## -syntax

````
NTSTATUS RxCeBuildAddress(
  _Inout_ PRXCE_ADDRESS               pAddress,
  _In_    PRXCE_TRANSPORT             pTransport,
  _In_    PTRANSPORT_ADDRESS          pTransportAddress,
  _In_    PRXCE_ADDRESS_EVENT_HANDLER pHandler,
  _In_    PVOID                       pEventContext
);
````


## -parameters
<dl>

### -param <i>pAddress</i> [in, out]

<dd>
<p>On input, this parameter contains a pointer to an uninitialized RDBSS connection engine address structure. On output when this call is successful, the data members in the RXCE_ADDRESS structure will be properly initialized.</p>
</dd>

### -param <i>pTransport</i> [in]

<dd>
<p>A pointer to the transport with which this address is to be associated.</p>
</dd>

### -param <i>pTransportAddress</i> [in]

<dd>
<p>A pointer to the transport address to be associated with the binding.</p>
</dd>

### -param <i>pHandler</i> [in]

<dd>
<p>A pointer to the event handler associated with the registration.</p>
</dd>

### -param <i>pEventContext</i> [in]

<dd>
<p>A pointer to the context parameter to be passed back to the event handler.</p>
</dd>
</dl>

## -returns
<p><b>RxCeBuildAddress</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The allocation of nonpaged pool memory needed by this routine failed. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameters passed to <b>RxCeBuildAddress</b> was invalid. </p>

<p> </p>

## -remarks
<p>When <b>RxCeBuildAddress</b> is successful, the data members in the RXCE_ADDRESS structure pointed to by the <i>pAddress</i> parameter will be properly initialized. </p>

<p>When <b>RxCeBuildAddress</b> is successful, the data members in the RXCE_ADDRESS structure pointed to by the <i>pAddress</i> parameter will be properly initialized. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553488">RxCeTearDownAddress</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeBuildAddress function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
