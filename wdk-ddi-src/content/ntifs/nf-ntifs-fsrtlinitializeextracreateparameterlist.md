---
UID : NF:ntifs.FsRtlInitializeExtraCreateParameterList
title : FsRtlInitializeExtraCreateParameterList function
author : windows-driver-content
description : The FsRtlInitializeExtraCreateParameterList routine initializes an extra create parameter (ECP) context structure list.
old-location : ifsk\fsrtlinitializeextracreateparameterlist.htm
old-project : ifsk
ms.assetid : 79e56363-1098-42bb-8e6a-c4b4c76e7e7c
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ifsk.fsrtlinitializeextracreateparameterlist, ntifs/FsRtlInitializeExtraCreateParameterList, FsRtlInitializeExtraCreateParameterList routine [Installable File System Drivers], FsRtlInitializeExtraCreateParameterList, fsrtlref_785d3f11-f568-491e-9cdb-abba70ae3eeb.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : The FsRtlInitializeExtraCreateParameterList routine is available starting with Windows 7.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : <= APC_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : TOKEN_TYPE
---


# FsRtlInitializeExtraCreateParameterList function
The <b>FsRtlInitializeExtraCreateParameterList</b> routine initializes an extra create parameter (ECP) context structure list.

## Syntax

````
NTSTATUS FsRtlInitializeExtraCreateParameterList(
  _Inout_ PECP_LIST EcpList
);
````

## Parameters

`EcpList`

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540148">ECP_LIST</a> structure to initialize.


## Return Value

<b>FsRtlInitializeExtraCreateParameterList</b> returns STATUS_SUCCESS if it successfully initialized the given <a href="https://msdn.microsoft.com/library/windows/hardware/ff540148">ECP_LIST</a> structure, and returns an error if it did not.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** |  |
| **IRQL** | <= APC_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540148">ECP_LIST</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlInitializeExtraCreateParameterList routine%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>