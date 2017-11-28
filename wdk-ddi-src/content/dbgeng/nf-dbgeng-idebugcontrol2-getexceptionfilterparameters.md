---
UID: NF.dbgeng.IDebugControl2.GetExceptionFilterParameters
title: IDebugControl2::GetExceptionFilterParameters
author: windows-driver-content
description: The GetExceptionFilterParameters method returns the parameters for exception filters specified by exception codes or by index.
old-location: debugger\getexceptionfilterparameters.htm
old-project: debugger
ms.assetid: 6c3db06a-0305-480f-ab7f-38e4295ebe9b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl2, GetExceptionFilterParameters, IDebugControl2::GetExceptionFilterParameters
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
req.alt-api: IDebugControl.GetExceptionFilterParameters,IDebugControl2.GetExceptionFilterParameters,IDebugControl3.GetExceptionFilterParameters
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

# IDebugControl2::GetExceptionFilterParameters method



## -description
<p>The <b>GetExceptionFilterParameters</b> method returns the parameters for exception filters specified by exception codes or by index.</p>


## -syntax

````
HRESULT GetExceptionFilterParameters(
  [in]           ULONG                              Count,
  [in, optional] PULONG                             Codes,
  [in]           ULONG                              Start,
  [out]          PDEBUG_EXCEPTION_FILTER_PARAMETERS Params
);
````


## -parameters
<dl>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of exception filters for which to return parameters.</p>
</dd>

### -param <i>Codes</i> [in, optional]

<dd>
<p>Specifies an array of exception codes.  The parameters for the exception filters with these exception codes will be returned.  If <i>Codes</i> is <b>NULL</b>, <i>Start</i> is used instead.</p>
</dd>

### -param <i>Start</i> [in]

<dd>
<p>Specifies the index of the first exception filter.  The parameters for the exception filters starting at <i>Start</i> will be returned.  If <i>Codes</i> is not <b>NULL</b>, <i>Start</i> is ignored.</p>
</dd>

### -param <i>Params</i> [out]

<dd>
<p>Receives the parameters for the exception filters specified by <i>Codes</i> or <i>Start</i>.  <i>Params</i> is an array of elements of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541485">DEBUG_EXCEPTION_FILTER_PARAMETERS</a>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about <a href="debugger.events#event_filters#event_filters">event filters</a>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543071">Event Filters</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fdb5059f-e7d9-4e14-aa3d-030e72c30732">sx, sxd, sxe, sxi, sxn (Set Exceptions)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556683">SetExceptionFilterParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548398">GetSpecificFilterParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetExceptionFilterParameters method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
