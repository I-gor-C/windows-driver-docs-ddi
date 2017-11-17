---
UID: NE.ndkpi._NDK_OPERATION_TYPE
title: NDK_OPERATION_TYPE
author: windows-driver-content
description: The NDK_OPERATION_TYPE enumeration defines types of NDK operations. Its enumeration values are used in the Type member of the NDK_RESULT_EX structure.
old-location: netvista\ndk_operation_type.htm
ms.assetid: EBB89BDA-6249-4D0F-A0EE-7074DDAFFFC1
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
req.iface: 
---

# NDK_OPERATION_TYPE enumeration



## -description
<p>The <b>NDK_OPERATION_TYPE</b> enumeration defines types of NDK operations. Its enumeration values are used in the <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265509">NDK_RESULT_EX</a> structure.</p>


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

### -field <a id="NdkOperationTypeReceive"></a><a id="ndkoperationtypereceive"></a><a id="NDKOPERATIONTYPERECEIVE"></a><b>NdkOperationTypeReceive</b>

<dd>
<p>An <i>NdkReceive</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439907">NDK_FN_RECEIVE</a>) operation.</p>
</dd>

### -field <a id="NdkOperationTypeReceiveAndInvalidate"></a><a id="ndkoperationtypereceiveandinvalidate"></a><a id="NDKOPERATIONTYPERECEIVEANDINVALIDATE"></a><b>NdkOperationTypeReceiveAndInvalidate</b>

<dd>
<p>An <i>NdkSendAndInvalidate</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/dn265507">NDK_FN_SEND_AND_INVALIDATE</a>) operation.</p>
</dd>

### -field <a id="NdkOperationTypeSend"></a><a id="ndkoperationtypesend"></a><a id="NDKOPERATIONTYPESEND"></a><b>NdkOperationTypeSend</b>

<dd>
<p>An <i>NdkSend</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439914">NDK_FN_SEND</a>) operation.</p>
</dd>

### -field <a id="NdkOperationTypeFastRegister"></a><a id="ndkoperationtypefastregister"></a><a id="NDKOPERATIONTYPEFASTREGISTER"></a><b>NdkOperationTypeFastRegister</b>

<dd>
<p>An <i>NdkFastRegister</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439887">NDK_FN_FAST_REGISTER</a>) operation.</p>
</dd>

### -field <a id="NdkOperationTypeBind"></a><a id="ndkoperationtypebind"></a><a id="NDKOPERATIONTYPEBIND"></a><b>NdkOperationTypeBind</b>

<dd>
<p>An <i>NdkBind</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439859">NDK_FN_BIND</a>)  operation.</p>
</dd>

### -field <a id="NdkOperationTypeInvalidate"></a><a id="ndkoperationtypeinvalidate"></a><a id="NDKOPERATIONTYPEINVALIDATE"></a><b>NdkOperationTypeInvalidate</b>

<dd>
<p>An <i>NdkInvalidate</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439901">NDK_FN_INVALIDATE</a>) operation.</p>
</dd>

### -field <a id="NdkOperationTypeRead"></a><a id="ndkoperationtyperead"></a><a id="NDKOPERATIONTYPEREAD"></a><b>NdkOperationTypeRead</b>

<dd>
<p>An <i>NdkRead</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439906">NDK_FN_READ</a>) operation.</p>
</dd>

### -field <a id="NdkOperationTypeWrite"></a><a id="ndkoperationtypewrite"></a><a id="NDKOPERATIONTYPEWRITE"></a><b>NdkOperationTypeWrite</b>

<dd>
<p>An <i>NdkWrite</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439917">NDK_FN_WRITE</a>) operation.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265509">NDK_RESULT_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_OPERATION_TYPE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
