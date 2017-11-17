---
UID: NF.wudfddi.IWDFNamedPropertyStore.SetNamedValue
title: IWDFNamedPropertyStore::SetNamedValue
author: windows-driver-content
description: The SetNamedValue method sets the value of a property.
old-location: wdf\iwdfnamedpropertystore_setnamedvalue.htm
ms.assetid: 1fd075c9-7d0e-4670-bac0-b7b8ba0a714f
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFNamedPropertyStore.SetNamedValue
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
ms.keywords: IWDFNamedPropertyStore, SetNamedValue, IWDFNamedPropertyStore::SetNamedValue
req.iface: IWDFNamedPropertyStore
req.product: Windows 10 or later.
---

# IWDFNamedPropertyStore::SetNamedValue method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>SetNamedValue</b> method sets the value of a property.</p>


## -syntax

````
HRESULT SetNamedValue(
  [in]       LPCWSTR     pszName,
  [in] const PROPVARIANT *pv
);
````


## -parameters
<dl>

### -param <i>pszName</i> [in]

<dd>
<p>A pointer to a null-terminated string that contains the name of the property.</p>
</dd>

### -param <i>pv</i> [in]

<dd>
<p>A pointer to the value that the property is set to. </p>
</dd>
</dl>

## -returns
<p><b>SetNamedValue</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>The following variant types are supported for property values. The following table shows the types of values that the framework writes for particular variant types.</p>

<p>VT_BSTR</p>

<p>Writes a string value.</p>

<p>VT_LPWSTR</p>

<p>VT_LPSTR</p>

<p>VT_I1</p>

<p>Writes an integer value.</p>

<p>VT_UI1</p>

<p>VT_I2</p>

<p>VT_UI2</p>

<p>VT_I4</p>

<p>VT_UI4</p>

<p>VT_UINT</p>

<p>VT_BLOB</p>

<p>Writes a binary value.</p>

<p>VT_VECTOR | VT_LPWSTR</p>

<p>Writes a string array.</p>

<p> </p>

<p>For more information, see <a href="wdf.using_the_registry_in_umdf_drivers">Using the Registry in UMDF-based Drivers</a>.</p>

<p>The following variant types are supported for property values. The following table shows the types of values that the framework writes for particular variant types.</p>

<p>VT_BSTR</p>

<p>Writes a string value.</p>

<p>VT_LPWSTR</p>

<p>VT_LPSTR</p>

<p>VT_I1</p>

<p>Writes an integer value.</p>

<p>VT_UI1</p>

<p>VT_I2</p>

<p>VT_UI2</p>

<p>VT_I4</p>

<p>VT_UI4</p>

<p>VT_UINT</p>

<p>VT_BLOB</p>

<p>Writes a binary value.</p>

<p>VT_VECTOR | VT_LPWSTR</p>

<p>Writes a string array.</p>

<p> </p>

<p>For more information, see <a href="wdf.using_the_registry_in_umdf_drivers">Using the Registry in UMDF-based Drivers</a>.</p>

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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560164">IWDFNamedPropertyStore</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFNamedPropertyStore::SetNamedValue method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
