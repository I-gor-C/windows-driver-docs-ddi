---
UID : NC:mrx.PMRX_EXTRACT_NETROOT_NAME
title : PMRX_EXTRACT_NETROOT_NAME
author : windows-driver-content
description : The MRxExtractNetRootName routine is called by RDBSS to request that a network mini-redirector extract the name of the NET_ROOT structure from a given pathname.
old-location : ifsk\mrxextractnetrootname.htm
old-project : ifsk
ms.assetid : e990b7fc-a341-419d-b358-eac4fa2dca78
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _SetDSMCounters_IN, SetDSMCounters_IN, *PSetDSMCounters_IN
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : mrx.h
req.include-header : Mrx.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : MRxExtractNetRootName
req.alt-loc : mrx.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : SetDSMCounters_IN, *PSetDSMCounters_IN
---


# PMRX_EXTRACT_NETROOT_NAME callback function
The<i> MRxExtractNetRootName</i> routine is called by <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs/the-rdbss-driver-and-library">RDBSS</a> to request that a network mini-redirector extract the name of the NET_ROOT structure from a given pathname.

## Syntax

```
PMRX_EXTRACT_NETROOT_NAME PmrxExtractNetrootName;

void PmrxExtractNetrootName(
  IN PUNICODE_STRING FilePathName,
  IN PMRX_SRV_CALL SrvCall,
  OUT PUNICODE_STRING NetRootName,
  OUT PUNICODE_STRING RestOfName OPTIONAL
)
{...}
```

## Parameters

`FilePathName`

A pointer to a Unicode string that contains a pathname.

`SrvCall`

A pointer to the SRV_CALL structure.

`NetRootName`

On input, a pointer for storing a Unicode string. On success, this parameter will contain a pointer to a Unicode string that contains a NET_ROOT structure name.

`OPTIONAL`




## Return Value

None

## Remarks

<i>MRxExtractNetRootName</i> parses the input name into the SRV_CALL structure, the NET_ROOT structure, and the rest of the pathname.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | mrx.h (include Mrx.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549864">MRxCreateSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549869">MRxCreateVNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550653">MRxFinalizeNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550656">MRxFinalizeSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550663">MRxFinalizeVNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550750">MRxPreparseName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550824">MRxSrvCallWinnerNotify</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxExtractNetRootName routine%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>