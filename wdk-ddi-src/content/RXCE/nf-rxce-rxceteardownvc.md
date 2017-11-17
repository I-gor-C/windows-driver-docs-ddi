---
UID: NF.rxce.RxCeTearDownVC
title: RxCeTearDownVC
author: windows-driver-content
description: RxCeTearDownVC deregisters a virtual circuit from a specified RDBSS connection.
old-location: ifsk\rxceteardownvc.htm
ms.assetid: d4b3af4d-8bb2-42a4-a8d9-baa643a90418
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
req.alt-api: RxCeTearDownVC
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
ms.keywords: RxCeTearDownVC
req.iface: 
req.product: Windows 10 or later.
---

# RxCeTearDownVC function



## -description
<p><b>RxCeTearDownVC</b> deregisters a virtual circuit from a specified RDBSS connection.</p>


## -syntax

````
NTSTATUS RxCeTearDownVC(
  _In_ PRXCE_VC pVc
);
````


## -parameters
<dl>

### -param <i>pVc</i> [in]

<dd>
<p>A pointer to a handle for an virtual circuit structure to be torn down. </p>
</dd>
</dl>

## -returns
<p><b>RxCeTearDownVC</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameters passed to this routine was invalid. </p>

<p> </p>

## -remarks
<p>When <b>RxCeTearDownVC</b> is successful, the data members in the RXCE_VC structure pointed to by the <i>pVC</i> parameter will be properly uninitialized and the virtual circuit will be disconnected from the associated RDBSS transport, address, and connection. </p>

<p>Note that <b>RxCeTearDownVC</b> will wait for the clean up of connections over other transports to be completed before returning.</p>

<p><b>RxCeTearDownVC</b> calls TDI to disconnect the virtual circuit associated with a connection. If the call to TDI is unsuccessful, <b>RxCeTearDownVC</b> will return the error from the TDI routine call. </p>

<p>When <b>RxCeTearDownVC</b> is successful, the data members in the RXCE_VC structure pointed to by the <i>pVC</i> parameter will be properly uninitialized and the virtual circuit will be disconnected from the associated RDBSS transport, address, and connection. </p>

<p>Note that <b>RxCeTearDownVC</b> will wait for the clean up of connections over other transports to be completed before returning.</p>

<p><b>RxCeTearDownVC</b> calls TDI to disconnect the virtual circuit associated with a connection. If the call to TDI is unsuccessful, <b>RxCeTearDownVC</b> will return the error from the TDI routine call. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553439">RxCeBuildVC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeTearDownVC function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
