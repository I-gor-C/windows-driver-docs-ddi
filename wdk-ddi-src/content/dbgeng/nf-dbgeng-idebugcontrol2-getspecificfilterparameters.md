---
UID: NF.dbgeng.IDebugControl2.GetSpecificFilterParameters
title: IDebugControl2::GetSpecificFilterParameters
author: windows-driver-content
description: The GetSpecificFilterParameters method returns the parameters for specific event filters.
old-location: debugger\getspecificfilterparameters.htm
old-project: debugger
ms.assetid: d2140270-558d-4cd9-b497-f61be40c7a87
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl2, GetSpecificFilterParameters, IDebugControl2::GetSpecificFilterParameters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.GetSpecificFilterParameters,IDebugControl2.GetSpecificFilterParameters,IDebugControl3.GetSpecificFilterParameters
req.alt-loc: dbgeng.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IDebugControl2
---

# IDebugControl2::GetSpecificFilterParameters method



## -description
<p>The <b>GetSpecificFilterParameters</b> method returns the parameters for specific event filters.</p>


## -syntax

````
HRESULT GetSpecificFilterParameters(
  [in]  ULONG                             Start,
  [in]  ULONG                             Count,
  [out] PDEBUG_SPECIFIC_FILTER_PARAMETERS Params
);
````


## -parameters
<dl>

### -param <i>Start</i> [in]

<dd>
<p>Specifies the index of the first specific event filter whose parameters will be returned.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of specific event filters to return parameters for.</p>
</dd>

### -param <i>Params</i> [out]

<dd>
<p>Receives the parameters for the specific event filters.  <i>Params</i> is an array of elements of type <a href="..\dbgeng\ns-dbgeng--debug-specific-filter-parameters.md">DEBUG_SPECIFIC_FILTER_PARAMETERS</a>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about <a href="debugger.events#event_filters#event_filters">event filters</a>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543071">Event Filters</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fdb5059f-e7d9-4e14-aa3d-030e72c30732">sx, sxd, sxe, sxi, sxn (Set Exceptions)</a>
</dt>
<dt>
<a href="debugger.setspecificfilterparameters">SetSpecificFilterParameters</a>
</dt>
<dt>
<a href="debugger.getexceptionfilterparameters">GetExceptionFilterParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetSpecificFilterParameters method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
