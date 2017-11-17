---
UID: NS.compstui._OIEXT
title: OIEXT
author: windows-driver-content
description: The OIEXT structure supplies additional, optional information about a property sheet page option that is described by an OPTITEM structure.
old-location: print\oiext.htm
ms.assetid: 932e5520-0ebf-4cfa-893a-a7eb969cb697
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: compstui.h
req.include-header: Compstui.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OIEXT
req.alt-loc: compstui.h
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
ms.keywords: OIEXT, OIEXT, *POIEXT
req.iface: 
---

# OIEXT structure



## -description
<p>The OIEXT structure supplies additional, optional information about a property sheet page option that is described by an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structure.</p>


## -syntax

````
typedef struct _OIEXT {
  WORD      cbSize;
  WORD      Flags;
  HINSTANCE hInstCaller;
  LPTSTR    pHelpFile;
  ULONG_PTR dwReserved[4];
} OIEXT, *POIEXT;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Size, in bytes, of the OIEXT structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Can contain the following bit flag:</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>OIEXTF_ANSI_STRING</p>
</td>
<td>
<p>If set, <b>pHelpFile</b> points to an ANSI string.</p>
<p>If not set, <b>pHelpFile</b> points to a Unicode string.</p>
<p>CPSUI does not check this flag if <b>pHelpFile</b> specifies a resource ID.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>hInstCaller</b>

<dd>
<p>Instance handle to a DLL containing string and icon resources belonging to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559670">OPTTYPE</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff559660">OPTPARAM</a> structures associated with the OIEXT structure. If <b>NULL</b>, CPSUI obtains resources from the DLL identified by the <b>hInstCaller</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546211">COMPROPSHEETUI</a> structure.</p>
</dd>

### -field <b>pHelpFile</b>

<dd>
<p>Pointer to a NULL-terminated string representing a path to a help file containing help information for the option. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero. If <b>NULL</b>, CPSUI uses the help file identified by the <b>pHelpFile</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546211">COMPROPSHEETUI</a> structure.</p>
</dd>

### -field <b>dwReserved</b>

<dd>
<p>Reserved, must be initialized to zero.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Compstui.h (include Compstui.h)</dt>
</dl>
</td>
</tr>
</table>