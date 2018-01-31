---
UID : NE:ndkpi._NDK_OPERATION_TYPE
title : "_NDK_OPERATION_TYPE"
author : windows-driver-content
description : The NDK_OPERATION_TYPE enumeration defines types of NDK operations. Its enumeration values are used in the Type member of the NDK_RESULT_EX structure.
old-location : netvista\ndk_operation_type.htm
old-project : netvista
ms.assetid : EBB89BDA-6249-4D0F-A0EE-7074DDAFFFC1
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : NdkOperationTypeSend, ndkpi/NdkOperationTypeFastRegister, ndkpi/NdkOperationTypeReceiveAndInvalidate, netvista.ndk_operation_type, NdkOperationTypeRead, NDK_OPERATION_TYPE enumeration [Network Drivers Starting with Windows Vista], ndkpi/NdkOperationTypeReceive, NdkOperationTypeFastRegister, ndkpi/NdkOperationTypeRead, _NDK_OPERATION_TYPE, NdkOperationTypeReceiveAndInvalidate, NdkOperationTypeInvalidate, NdkOperationTypeReceive, ndkpi/NdkOperationTypeSend, NdkOperationTypeBind, ndkpi/NdkOperationTypeWrite, ndkpi/NdkOperationTypeBind, NdkOperationTypeWrite, ndkpi/NDK_OPERATION_TYPE, ndkpi/NdkOperationTypeInvalidate, NDK_OPERATION_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ndkpi.h
req.include-header : Ndkpi.h
req.target-type : Windows
req.target-min-winverclnt : None supported,Supported in NDIS 6.40 and later.
req.target-min-winversvr : Windows Server 2012 R2
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : "<=DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : NDK_OPERATION_TYPE
---

# _NDK_OPERATION_TYPE Enumeration
The <b>NDK_OPERATION_TYPE</b> enumeration defines types of NDK operations. Its enumeration values are used in the <b>Type</b> member of the <a href="..\ndkpi\ns-ndkpi-_ndk_result_ex.md">NDK_RESULT_EX</a> structure.

## Syntax
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

## Constants

<table>

<tr>
<td>NdkOperationTypeBind</td>
<td>An <i>NdkBind</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_bind.md">NDK_FN_BIND</a>)  operation.</td>
</tr>

<tr>
<td>NdkOperationTypeFastRegister</td>
<td>An <i>NdkFastRegister</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_fast_register.md">NDK_FN_FAST_REGISTER</a>) operation.</td>
</tr>

<tr>
<td>NdkOperationTypeInvalidate</td>
<td>An <i>NdkInvalidate</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_invalidate.md">NDK_FN_INVALIDATE</a>) operation.</td>
</tr>

<tr>
<td>NdkOperationTypeRead</td>
<td>An <i>NdkRead</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_read.md">NDK_FN_READ</a>) operation.</td>
</tr>

<tr>
<td>NdkOperationTypeReceive</td>
<td>An <i>NdkReceive</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_receive.md">NDK_FN_RECEIVE</a>) operation.</td>
</tr>

<tr>
<td>NdkOperationTypeReceiveAndInvalidate</td>
<td>An <i>NdkSendAndInvalidate</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_send_and_invalidate.md">NDK_FN_SEND_AND_INVALIDATE</a>) operation.</td>
</tr>

<tr>
<td>NdkOperationTypeSend</td>
<td>An <i>NdkSend</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_send.md">NDK_FN_SEND</a>) operation.</td>
</tr>

<tr>
<td>NdkOperationTypeWrite</td>
<td>An <i>NdkWrite</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_write.md">NDK_FN_WRITE</a>) operation.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndkpi.h (include Ndkpi.h) |

## See Also

<a href="..\ndkpi\ns-ndkpi-_ndk_result_ex.md">NDK_RESULT_EX</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_OPERATION_TYPE enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>