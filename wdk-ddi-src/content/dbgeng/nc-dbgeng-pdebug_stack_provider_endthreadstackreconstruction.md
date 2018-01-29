---
UID : NC:dbgeng.PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION
title : PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION
author : windows-driver-content
description : The EndThreadStackReconstruction callback function may be called after stack reconstruction to clean up state.
old-location : debugger\endthreadstackreconstruction.htm
old-project : debugger
ms.assetid : 76984F28-7AC9-44FD-9D8B-CC184484C73E
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : debugger.endthreadstackreconstruction, EndThreadStackReconstruction, EndThreadStackReconstruction callback function [Windows Debugging], EndThreadStackReconstruction, PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION, PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION, dbgeng/EndThreadStackReconstruction
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : dbgeng.h
req.include-header : Dbgeng.h
req.target-type : Windows
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
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---


# PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION callback function
The <i>EndThreadStackReconstruction</i> callback function may be called after stack reconstruction to clean up state.
<div class="code"><span codelanguage="ManagedCPlusPlus"><table>
<tr>
<th>C++</th>
</tr>
<tr>
<td>
<pre> CALLBACK* PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION EndThreadStackReconstruction;</pre>
</td>
</tr>
</table></span></div>

## Syntax

```
PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION PdebugStackProviderEndthreadstackreconstruction;

HRESULT PdebugStackProviderEndthreadstackreconstruction(
   void
)
{...}
```

## Parameters

`void`




## Return Value

If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.

## Remarks

<i>EndThreadStackReconstruction</i> is called <b>PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION</b> in the Dbgeng.h header file.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |