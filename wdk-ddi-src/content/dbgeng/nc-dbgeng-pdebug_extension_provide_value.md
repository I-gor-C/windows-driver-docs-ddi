---
UID : NC:dbgeng.PDEBUG_EXTENSION_PROVIDE_VALUE
title : PDEBUG_EXTENSION_PROVIDE_VALUE
author : windows-driver-content
description : The DebugExtensionProvideValue callback function sets pseudo-register values.C++ CALLBACK* PDEBUG_EXTENSION_PROVIDE_VALUE DebugExtensionProvideValue;
old-location : debugger\debugextensionprovidevalue.htm
old-project : debugger
ms.assetid : b4b1953c-dc1b-495a-ab58-5cfaa6064b23
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _DOT4_ACTIVITY, *PDOT4_ACTIVITY, DOT4_ACTIVITY
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : dbgeng.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DebugExtensionProvideValue
req.alt-loc : Dbgeng.h
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
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---


# PDEBUG_EXTENSION_PROVIDE_VALUE callback function
The <b>DebugExtensionProvideValue</b> callback function sets <a href="https://msdn.microsoft.com/fa334c9f-46c6-4288-95ce-43128fff7f03">pseudo-register</a> values.

## Syntax

```
PDEBUG_EXTENSION_PROVIDE_VALUE PdebugExtensionProvideValue;

HRESULT PdebugExtensionProvideValue(
  PDEBUG_CLIENT Client,
  ULONG Flags,
  PCWSTR Name,
  PULONG64 Value,
  PULONG64 TypeModBase,
  PULONG TypeId,
  PULONG TypeFlags
)
{...}
```

## Parameters

`Client`

A client to use if the extension needs DbgEng functions.

`Flags`

Provides behavioral flags. This parameter is currently reserved.

`Name`

The name of the value to return. This name might be one of the names that the <a href="..\dbgeng\nc-dbgeng-pdebug_extension_query_value_names.md">DebugExtensionQueryValueNames</a> function returned or a name that the caller might already be aware of.

`Value`

A pointer to the value to be set.

`TypeModBase`

The base starting address for <i>Client.</i>

`TypeId`

A pointer to the ID for the type of <i>Value</i>.

`TypeFlags`

A parameter that you can use to return one of the following flags: 

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>


## Return Value

<b>DebugExtensionProvideValue</b> might return one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The function was successfully completed.

 

This function might also return error values. For more information about possible return values, see <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a>.

## Remarks

The name that the <i>Name</i> parameter specifies must start with <b>$$</b> and have a terminating NULL character. 

<i>DebugExtensionProvideValue</i> is called <b>PDEBUG_EXTENSION_PROVIDE_VALUE</b> in the Dbgeng.h header file.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\dbgeng\nc-dbgeng-pdebug_extension_initialize.md">DebugExtensionInitialize</a>
</dt>
<dt><i>DebugExtensionNotify</i></dt>
<dt><i>DebugExtensionQueryValueNames</i></dt>
<dt><i>DebugExtensionUninitialize</i></dt>
<dt><i>KnownStructOutput</i></dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20PDEBUG_EXTENSION_PROVIDE_VALUE callback function%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>