---
UID : NS:ndkpi._NDK_SRQ_DISPATCH
title : _NDK_SRQ_DISPATCH
author : windows-driver-content
description : The NDK_SRQ_DISPATCH structure specifies dispatch function entry points for the NDK shared receive queue (SRQ) object.
old-location : netvista\ndk_srq_dispatch.htm
old-project : netvista
ms.assetid : 13297898-A72B-4771-A022-FDCBC281CEA0
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDK_SRQ_DISPATCH, NDK_SRQ_DISPATCH
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ndkpi.h
req.include-header : Ndkpi.h
req.target-type : Windows
req.target-min-winverclnt : None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NDK_SRQ_DISPATCH
req.alt-loc : ndkpi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <=DISPATCH_LEVEL
req.typenames : NDK_SRQ_DISPATCH
---

# _NDK_SRQ_DISPATCH structure
The <b>NDK_SRQ_DISPATCH</b> structure specifies dispatch function entry points for the NDK shared receive queue (SRQ) object.

## Syntax
````
typedef struct _NDK_SRQ_DISPATCH {
  NDK_FN_CLOSE_OBJECT              NdkCloseSrq;
  NDK_FN_QUERY_EXTENSION_INTERFACE NdkQueryExtension;
  NDK_FN_MODIFY_SRQ                NdkModifySrq;
  NDK_FN_SRQ_RECEIVE               NdkSrqReceive;
} NDK_SRQ_DISPATCH;
````

## Members

        
            `NdkCloseSrq`

            The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk_fn_close_object.md">NDK_FN_CLOSE_OBJECT</a> dispatch function.
        
            `NdkModifySrq`

            The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk_fn_modify_srq.md">NDK_FN_MODIFY_SRQ</a> dispatch function.
        
            `NdkQueryExtension`

            The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk_fn_query_extension_interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a> dispatch function.
        
            `NdkSrqReceive`

            The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk_fn_srq_receive.md">NDK_FN_SRQ_RECEIVE</a> dispatch function.

    ## Remarks
        The <b>NDK_SRQ_DISPATCH</b> structure is used in the <a href="..\ndkpi\ns-ndkpi-_ndk_srq.md">NDK_SRQ</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndkpi.h (include Ndkpi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_srq.md">NDK_SRQ</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_close_object.md">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_modify_srq.md">NDK_FN_MODIFY_SRQ</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_query_extension_interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_srq_receive.md">NDK_FN_SRQ_RECEIVE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_SRQ_DISPATCH structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>