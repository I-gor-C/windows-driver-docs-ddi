---
UID: NS.compstui._OPTTYPE
title: OPTTYPE
author: windows-driver-content
description: The OPTTYPE structure is used by CPSUI applications (including printer interface DLLs) for describing the type and other characteristics of a property sheet option, if the option is specified by an OPTITEM structure.
old-location: print\opttype.htm
ms.assetid: 041dd438-e837-4912-bda7-de654204198b
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
req.alt-api: OPTTYPE
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
ms.keywords: OPTTYPE, OPTTYPE, *POPTTYPE
req.iface: 
---

# OPTTYPE structure



## -description
<p>The OPTTYPE structure is used by CPSUI applications (including printer interface DLLs) for describing the type and other characteristics of a <a href="https://msdn.microsoft.com/572330d6-1a1b-46fd-bfb4-be2b0990bca4">property sheet option</a>, if the option is specified by an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structure.</p>


## -syntax

````
typedef struct _OPTTYPE {
  WORD      cbSize;
  BYTE      Type;
  BYTE      Flags;
  WORD      Count;
  WORD      BegCtrlID;
  POPTPARAM pOptParam;
  WORD      Style;
  WORD      wReserved[3];
  ULONG_PTR dwReserved[3];
} OPTTYPE, *POPTTYPE;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Size, in bytes, of the OPTTYPE structure.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/3b3c002c-a201-4f81-b208-30864343409b">CPSUI option type</a>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Optional bit flags that modify the option's characteristics. The following flags can be set in any combination.</p>
<p></p>
<dl>

### -field <a id="OPTTF_NOSPACE_BEFORE_POSTFIX"></a><a id="opttf_nospace_before_postfix"></a>OPTTF_NOSPACE_BEFORE_POSTFIX

<dd>
<p>CPSUI should not add a space character between the string specified by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structure's <b>pName</b> string and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559660">OPTPARAM</a> structure's <b>pData</b> string, when displaying the option.</p>
<p>Valid only if the option type is or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562847">TVOT_SCROLLBAR</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562848">TVOT_TRACKBAR</a>.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTTF_TYPE_DISABLED"></a><a id="opttf_type_disabled"></a>OPTTF_TYPE_DISABLED

<dd>
<p>All the OPTPARAM structures to which <b>pOptParam</b> points are disabled, so that none of the parameter values are user-selectable.</p>
</dd>
</dl>
</dd>

### -field <b>Count</b>

<dd>
<p>Specifies the number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559660">OPTPARAM</a> structures to which <b>pOptParam</b> points. This member's value is dependent on the <a href="https://msdn.microsoft.com/3b3c002c-a201-4f81-b208-30864343409b">CPSUI option type</a>.</p>
</dd>

### -field <b>BegCtrlID</b>

<dd>
<p>If <b>pDlgPage</b> in <a href="https://msdn.microsoft.com/library/windows/hardware/ff546211">COMPROPSHEETUI</a> identifies a CPSUI-supplied page, or if <b>DlgTemplateID</b> in <a href="https://msdn.microsoft.com/library/windows/hardware/ff547607">DLGPAGE</a> identifies a CPSUI-supplied template, <b>BegCtrlID</b> is not used.</p>
<p>Otherwise, <b>BegCtrlID</b> must contain the first of a sequentially numbered set of Windows control identifiers. Control identifier usage is dependent on the <a href="https://msdn.microsoft.com/3b3c002c-a201-4f81-b208-30864343409b">CPSUI option type</a>.</p>
</dd>

### -field <b>pOptParam</b>

<dd>
<p>Pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559660">OPTPARAM</a> structures describing the parameter values that a user can select for the option.</p>
</dd>

### -field <b>Style</b>

<dd>
<p>Specifies flags that can be used to modify the option's display characteristics. The flags that can be specified are dependent on the <a href="https://msdn.microsoft.com/3b3c002c-a201-4f81-b208-30864343409b">CPSUI option type</a>.</p>
</dd>

### -field <b>wReserved</b>

<dd>
<p>Reserved, must be initialized to zero.</p>
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