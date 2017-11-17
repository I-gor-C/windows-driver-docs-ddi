---
UID: NF.dbgeng.IDebugDataSpaces4.ReadHandleData
title: IDebugDataSpaces4::ReadHandleData
author: windows-driver-content
description: The ReadHandleData method retrieves information about a system object specified by a system handle.
old-location: debugger\readhandledata.htm
ms.assetid: 9ad8e8c1-6aee-4eac-93e6-5997212c63d0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces2.ReadHandleData,IDebugDataSpaces3.ReadHandleData,IDebugDataSpaces4.ReadHandleData
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
ms.keywords: IDebugDataSpaces4, ReadHandleData, IDebugDataSpaces4::ReadHandleData
req.iface: IDebugDataSpaces4
---

# IDebugDataSpaces4::ReadHandleData method



## -description
<p>The <b>ReadHandleData</b> method retrieves information about a system object specified by a system handle.</p>


## -syntax

````
HRESULT ReadHandleData(
  [in]            ULONG64 Handle,
  [in]            ULONG   DataType,
  [out, optional] PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  DataSize
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Specifies the system handle of the object whose data is requested.  See Handles for information about system handles.</p>
</dd>

### -param <i>DataType</i> [in]

<dd>
<p>Specifies the data type to return for the system handle.  The following table contains the valid values, along with the corresponding return type:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_HANDLE_DATA_TYPE_BASIC</p>
</td>
<td>
<p>Returns basic information about the system object.</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type <a href="https://msdn.microsoft.com/c1ad22b9-9733-417a-96ae-bc5920462f4f">PDEBUG_HANDLE_DATA_BASIC</a>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_HANDLE_DATA_TYPE_TYPE_NAME</p>
</td>
<td>
<p>Returns the name of the object type.  For example, "Process" or "Thread".</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PSTR.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_HANDLE_DATA_TYPE_OBJECT_NAME</p>
</td>
<td>
<p>Returns the name of the object.  This includes its location in the object directory.</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PSTR.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_HANDLE_DATA_TYPE_HANDLE_COUNT</p>
</td>
<td>
<p>Returns the number of handles held by the object.  This is similar to the field <a href="https://msdn.microsoft.com/library/windows/hardware/ff541500">DEBUG_HANDLE_DATA_BASIC</a>.<b>HandleCount</b>.</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PULONG.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_HANDLE_DATA_TYPE_TYPE_NAME_WIDE</p>
</td>
<td>
<p>Returns the name of the object type.</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PWSTR</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_HANDLE_DATA_TYPE_OBJECT_NAME_WIDE</p>
</td>
<td>
<p>Returns the name of the object.</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PWSTR.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the object data.  Upon successful completion of the method, the contents of this buffer may be accessed by casting <i>Buffer</i> to the type specified in the above table.</p>
<p>If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be returned.</p>
</dd>

### -param <i>DataSize</i> [out, optional]

<dd>
<p>Receives the size of the data in bytes.  If <i>DataSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p>

## -remarks
<p>This method is only available in user-mode debugging.</p>

<p>This method is only available in user-mode debugging.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550531">IDebugDataSpaces2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550537">IDebugDataSpaces3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550546">IDebugDataSpaces4</a>
</dt>
<dt>Handles</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces2::ReadHandleData method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
