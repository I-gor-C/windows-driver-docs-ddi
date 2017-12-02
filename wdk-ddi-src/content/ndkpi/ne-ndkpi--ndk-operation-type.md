---
UID: NE.ndkpi._NDK_OPERATION_TYPE
title: NDK_OPERATION_TYPE
author: windows-driver-content
description: The NDK_OPERATION_TYPE enumeration defines types of NDK operations. Its enumeration values are used in the Type member of the NDK_RESULT_EX structure.
old-location: netvista\ndk_operation_type.htm
old-project: netvista
ms.assetid: EBB89BDA-6249-4D0F-A0EE-7074DDAFFFC1
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.40 and later.
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDK_OPERATION_TYPE
req.alt-loc: ndkpi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# NDK_OPERATION_TYPE enumeration



## -description
<p>The <b>NDK_OPERATION_TYPE</b> enumeration defines types of NDK operations. Its enumeration values are used in the <b>Type</b> member of the <a href="..\ndkpi\ns-ndkpi--ndk-result-ex.md">NDK_RESULT_EX</a> structure.</p>


## -syntax

````
typedef enum _NDK_OPERATION_TYPE { 
  NdkOperationTypeReceive               = 1,
  NdkOperationTypeReceiveAndInvalidate  = 32769,
  NdkOperationTypeSend                  = 2,
  NdkOperationTypeFastRegister          = 4,
  NdkOperationTypeBind                  = 8,
  NdkOperationTypeInvalidate            = 16,
  NdkOperationTypeRead                  = 32,
  NdkOperationTypeWrite                 = 64
} NDK_OPERATION_TYPE;
````


## -enum-fields
<dl>

### -field NdkOperationTypeReceive

<dd>
<p>An <i>NdkReceive</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-receive.md">NDK_FN_RECEIVE</a>) operation.</p>
</dd>

### -field NdkOperationTypeReceiveAndInvalidate

<dd>
<p>An <i>NdkSendAndInvalidate</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-send-and-invalidate.md">NDK_FN_SEND_AND_INVALIDATE</a>) operation.</p>
</dd>

### -field NdkOperationTypeSend

<dd>
<p>An <i>NdkSend</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-send.md">NDK_FN_SEND</a>) operation.</p>
</dd>

### -field NdkOperationTypeFastRegister

<dd>
<p>An <i>NdkFastRegister</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-fast-register.md">NDK_FN_FAST_REGISTER</a>) operation.</p>
</dd>

### -field NdkOperationTypeBind

<dd>
<p>An <i>NdkBind</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-bind.md">NDK_FN_BIND</a>)  operation.</p>
</dd>

### -field NdkOperationTypeInvalidate

<dd>
<p>An <i>NdkInvalidate</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-invalidate.md">NDK_FN_INVALIDATE</a>) operation.</p>
</dd>

### -field NdkOperationTypeRead

<dd>
<p>An <i>NdkRead</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-read.md">NDK_FN_READ</a>) operation.</p>
</dd>

### -field NdkOperationTypeWrite

<dd>
<p>An <i>NdkWrite</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-write.md">NDK_FN_WRITE</a>) operation.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.40 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndkpi.h (include Ndkpi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-result-ex.md">NDK_RESULT_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_OPERATION_TYPE enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
