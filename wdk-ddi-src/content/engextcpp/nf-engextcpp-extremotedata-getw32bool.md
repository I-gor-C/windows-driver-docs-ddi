---
UID : NF:engextcpp.ExtRemoteData.GetW32Bool
title : ExtRemoteData::GetW32Bool method
author : windows-driver-content
description : The GetW32Bool method returns a BOOL version of the ExtRemoteData object, which represents the contents of the target's memory.
old-location : debugger\extremotedata_getw32bool.htm
old-project : debugger
ms.assetid : a17812f5-4e20-4793-9352-3cabed25a6da
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : GetW32Bool method [Windows Debugging], ExtRemoteData class, GetW32Bool method [Windows Debugging], ExtRemoteData, GetW32Bool, EngExtCpp_Ref_367ee79b-5fdf-41ca-b43c-f9f29b3a872c.xml, ExtRemoteData class [Windows Debugging], GetW32Bool method, debugger.extremotedata_getw32bool, ExtRemoteData::GetW32Bool
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
req.typenames : "*PSILO_DRIVER_CAPABILITIES, SILO_DRIVER_CAPABILITIES"
---


# GetW32Bool method
The <b>GetW32Bool</b> method returns a BOOL version of the <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> object, which represents the contents of the target's memory.

## Syntax

````
BOOL GetW32Bool();
````

## Parameters

This function has no parameters.

## Return Value

<b>GetW32Bool</b> returns the BOOL version of  the <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> object.

## Remarks

The size of the memory represented by the <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> object must be <code>sizeof(BOOL)</code>.
<div class="alert"><b>Note</b>    There are several different types that can be used to represent a Boolean value. BOOL is one of these types.  For the C++ <b>bool</b> type, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544050">ExtRemoteData::GetStdBool</a>.  For the BOOLEAN type, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544013">ExtRemoteData::GetBoolean</a>.</div><div> </div>

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

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544019">ExtRemoteData::GetData</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544013">ExtRemoteData::GetBoolean</a>

<a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544050">ExtRemoteData::GetStdBool</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20ExtRemoteData.GetW32Bool method%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>