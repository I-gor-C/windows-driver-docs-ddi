---
UID: NF.engextcpp.ExtRemoteData.WriteBuffer
title: ExtRemoteData::WriteBuffer
author: windows-driver-content
description: The WriteBuffer method writes data to the target's memory. The data is located in the beginning of the region represented by the ExtRemoteData object. However, the size of the data can be different.
old-location: debugger\extremotedata_writebuffer.htm
ms.assetid: b50f0cf3-4cd5-4f9e-9749-49b1c9365a8f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: engextcpp.hpp
req.include-header: Engextcpp.hpp
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExtRemoteData.WriteBuffer
req.alt-loc: engextcpp.hpp
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
ms.keywords: ExtRemoteData, WriteBuffer, ExtRemoteData::WriteBuffer
req.iface: ExtRemoteData
---

# ExtRemoteData::WriteBuffer method



## -description
<p>The <b>WriteBuffer</b> method writes data to the target's memory.  The data is located in the beginning of the region represented by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544008">ExtRemoteData</a> object.  However, the size of the data can be different.</p>


## -syntax

````
ULONG WriteBuffer(
  [in] PVOID Buffer,
  [in] ULONG Bytes,
  [in] bool  MustReadAll
);
````


## -parameters
<dl>

### -param <i>Buffer</i> [in]

<dd>
<p>Specifies the data to write to the target.</p>
</dd>

### -param <i>Bytes</i> [in]

<dd>
<p>Specifies the number of bytes to write.  The <i>Buffer</i> buffer must be at least this size.</p>
</dd>

### -param <i>MustReadAll</i> [in]

<dd>
<p>Specifies what happens if the debugger engine is unable to write all the data to the target.  If <i>MustReadAll</i> is <code>true</code> and the debugger engine is unable to write <i>Bytes</i> bytes to the target, an <b>ExtRemoteException</b> will be thrown.  If <i>MustReadAll</i> is <code>false</code>, no exception will be thrown if the engine is unable to write the requested number of bytes to the target.</p>
</dd>
</dl>

## -returns
<p><b>WriteBuffer</b> returns the number of bytes written to the target from the <i>Buffer</i> buffer.  If <i>MustReadAll</i> is <code>true</code>, the value of <i>Bytes</i> will be returned (unless an exception is thrown).</p>

## -remarks


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
<dt>Engextcpp.hpp (include Engextcpp.hpp)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544008">ExtRemoteData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544088">ExtRemoteData::ReadBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20ExtRemoteData.WriteBuffer method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
