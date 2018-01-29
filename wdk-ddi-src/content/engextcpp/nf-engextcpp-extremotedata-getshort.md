---
UID : NF:engextcpp.ExtRemoteData.GetShort
title : ExtRemoteData::GetShort method
author : windows-driver-content
description : The GetShort method returns a SHORT version of the ExtRemoteData object, which represents the contents of the target's memory.
old-location : debugger\extremotedata_getshort.htm
old-project : debugger
ms.assetid : 5e364e83-76db-44b0-b5bc-15eed53bbbdf
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : GetShort method [Windows Debugging], ExtRemoteData class, debugger.extremotedata_getshort, ExtRemoteData, ExtRemoteData::GetShort, ExtRemoteData class [Windows Debugging], GetShort method, GetShort, GetShort method [Windows Debugging], EngExtCpp_Ref_c2fffdd2-e899-4f87-bd00-415bafa3b84f.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : engextcpp.hpp
req.include-header : Engextcpp.hpp
req.target-type : Desktop
req.target-min-winverclnt : 
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
req.lib : engextcpp.hpp
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : SILO_DRIVER_CAPABILITIES, *PSILO_DRIVER_CAPABILITIES
---


# GetShort method
The <b>GetShort</b> method returns a SHORT version of the <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> object, which represents the contents of the target's memory.

## Syntax

````
SHORT GetShort();
````

## Parameters

This function has no parameters.

## Return Value

<b>GetShort</b> returns the SHORT version of the <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> object.

## Remarks

The size of the memory represented by the <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> object must be <code>sizeof(SHORT)</code>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | engextcpp.hpp (include Engextcpp.hpp) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544077">ExtRemoteData::GetUshort</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544019">ExtRemoteData::GetData</a>

<a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20ExtRemoteData.GetShort method%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>