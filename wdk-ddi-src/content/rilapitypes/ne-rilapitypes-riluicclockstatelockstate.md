---
UID : NE:rilapitypes.RILUICCLOCKSTATELOCKSTATE
title : RILUICCLOCKSTATELOCKSTATE
author : windows-driver-content
description : This enumeration describes the RILUICCLOCKSTATELOCKSTATE.
old-location : netvista\riluicclockstatelockstate.htm
old-project : netvista
ms.assetid : 95f73081-b809-407d-b73b-975b97301449
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILUICCLOCKSTATELOCKSTATE, RILUICCLOCKSTATELOCKSTATE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : rilapitypes.h
req.include-header : Rilapitypes.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILUICCLOCKSTATELOCKSTATE
req.alt-loc : rilapitypes.h
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
req.typenames : RILUICCLOCKSTATELOCKSTATE
req.product : Windows 10 or later.
---

# RILUICCLOCKSTATELOCKSTATE Enumeration


## Syntax
````
enum RILUICCLOCKSTATELOCKSTATE {
  RIL_PARAM_UICCLOCKSTATE_LOCKSTATE  = 0x0000000, 
  RIL_UICCLOCKSTATE_VERIFIED         = 0x0000001, 
  RIL_UICCLOCKSTATE_ENABLED          = 0x0000002, 
  RIL_UICCLOCKSTATE_BLOCKED          = 0x0000003 

};
````

## Constants

<table>

<tr>
<td>RIL_UICCLOCKSTATE_BLOCKED</td>
<td>Lock is blocked.</td>
</tr>

<tr>
<td>RIL_UICCLOCKSTATE_ENABLED</td>
<td>Lock is enabled.</td>
</tr>

<tr>
<td>RIL_UICCLOCKSTATE_VERIFIED</td>
<td>Lock is verified.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h (include Rilapitypes.h) |

## See Also

<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn946509">Cellular COM enumerations</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20RILUICCLOCKSTATELOCKSTATE enumeration%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>