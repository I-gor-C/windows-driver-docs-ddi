---
UID: NC.d3d10umddi.PFND3D11_1DDI_QUERYAUTHENTICATEDCHANNEL
title: PFND3D11_1DDI_QUERYAUTHENTICATEDCHANNEL
author: windows-driver-content
description: Queries an authenticated channel for capability and state information. Implemented by a Windows Display Driver Model (WDDM) 1.2 or later user-mode display driver.
old-location: display\queryauthenticatedchannel1.htm
old-project: display
ms.assetid: bb152e3d-497f-4798-86cc-6f300e24a05c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: QueryAuthenticatedChannel
req.alt-loc: D3d10umddi.h
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
req.iface: 
---

# PFND3D11_1DDI_QUERYAUTHENTICATEDCHANNEL callback



## -description
<p>Queries an authenticated channel for capability and state information. Implemented by a Windows Display Driver Model (WDDM) 1.2 or later user-mode display driver.</p>


## -prototype

````
PFND3D11_1DDI_QUERYAUTHENTICATEDCHANNEL QueryAuthenticatedChannel;

HRESULT APIENTRY* QueryAuthenticatedChannel(
  _In_        D3D10DDI_HDEVICE        hDevice,
  _In_        D3D11_1DDI_HAUTHCHANNEL hCAuthChannel,
  _In_        UINT                    InputDataSize,
  _Out_ const VOID                    *pInputData,
  _In_        UINT                    OutputDataSize,
  _Out_       VOID                    *pOutputData
)
{ ... }
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p>A handle to the display device (graphics context).

</p>
</dd>

### -param hCAuthChannel [in]

<dd>
<p>A handle to an authenticated channel object that was created through a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createauthenticatedchannel.md">CreateAuthenticatedChannel(D3D11_1)</a> function.</p>
</dd>

### -param InputDataSize [in]

<dd>
<p>The size, in bytes, of the data in the <i>pInputData</i> array.

</p>
</dd>

### -param pInputData [out]

<dd>
<p>A pointer to a buffer that describes the information to query. The data in this buffer is formatted as a <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-input.md">D3D11_1DDI_AUTHENTICATED_QUERY_INPUT</a> structure.</p>
</dd>

### -param OutputDataSize [in]

<dd>
<p>The size, in bytes, of the data in the <i>pOutputData</i> array.

</p>
</dd>

### -param pOutputData [out]

<dd>
<p>A pointer to a buffer that contains the queried information. For more information, see the Remarks section.</p>
</dd>
</dl>

## -returns
<p>Returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The authenticated channel was queried successfully.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The display miniport driver does not support the specified command</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
        Memory was not available to complete the operation.</p>

<p> </p>

## -remarks
<p>The <i>pInputData</i> parameter references a buffer that contains a <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-input.md">D3D11_1DDI_AUTHENTICATED_QUERY_INPUT</a> structure. This structure contains the driver's handle to the authenticated channel, a sequence number, and a GUID that indicates the type of query to perform.  The driver must return  <b>E_INVALIDARG</b> if the sequence number was not previously initialized by using the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-configureauthenticatedchannel.md">ConfigureAuthenticatedChannel(D3D11_1)</a> function.  The driver must  also return  <b>E_INVALIDARG</b> if the sequence number is not greater than the sequence number of the previous query call.

</p>

<p>The byte array that is referenced by the <i>pOutputData</i> parameter is in a format that is specified by the <b>QueryType</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-input.md">D3D11_1DDI_AUTHENTICATED_QUERY_INPUT</a> structure. The following list describes the format of this data based on the <b>QueryType</b> member.</p>

<p></p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-protection-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_PROTECTION_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-channel-type-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-device-handle-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_DEVICE_HANDLE_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-crypto-session-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_CRYPTO_SESSION_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-restricted-shared-resource-process-count-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_COUNT_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-restricted-shared-resource-process-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-unrestricted-protected-shared-resource-count-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_UNRESTRICTED_PROTECTED_SHARED_RESOURCE_COUNT_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-output-id-count-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-output-id-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-acessibility-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_ACESSIBILITY_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-accessibility-encryption-guid-count-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_COUNT_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-accessibility-encryption-guid-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT</a>
</p>

<p>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-current-accessibility-encryption-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_CURRENT_ACCESSIBILITY_ENCRYPTION_OUTPUT</a>
</p>

<p>The driver prepares the output buffer that is referenced by the <i>pOutputData</i> parameter by following these steps:</p>

<p>Each structure that is returned based on the <b>QueryType</b> member starts with a <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</a> structure. The driver must copy the members of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-input.md">D3D11_1DDI_AUTHENTICATED_QUERY_INPUT</a> to the <b>D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</b> structure. </p>

<p>The driver must set the  <b>ReturnCode</b> member to the same return code that it will return for the <i>QueryAuthenticatedChannel(D3D11_1)</i> call. This provides the application with a secure mechanism of accessing the return code. 

</p>

<p>Based on the value of the <b>QueryType</b> member, the driver must initialize the corresponding structure that follows the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</a> structure in the <i>pOutputData</i> buffer.</p>

<p>The driver must sign the <i>pOutputData</i> buffer in a way that is identical to the way it handles Output Protection Manager (OPM) queries.</p>

<p>The <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</a> structure contains an AES-based one-key CBC message authentication code (OMAC) of the data. The display miniport driver must calculate an OMAC over the data in the output buffer to authenticate the data. The driver does this by first setting the <b>omac</b> member to zero and then calculating an OMAC for the data in the buffer. The driver then sets the <b>omac</b> member to the OMAC that it calculated.</p>

<p>The display miniport driver must return  <b>E_INVALIDARG</b> for the <i>QueryAuthenticatedChannel(D3D11_1)</i> call under the following conditions:</p>

<p>The sequence number is not greater than a sequence number that was specified in a previous configuration call.</p>

<p>The sequence number has not yet been initialized by a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-configureauthenticatedchannel.md">ConfigureAuthenticatedChannel(D3D11_1)</a> function.

</p>

<p>The <i>OutputDataSize</i> parameter is less than size of the structure specified by the  <b>D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT.QueryType</b> member.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-configureauthenticatedchannel.md">ConfigureAuthenticatedChannel(D3D11_1)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createauthenticatedchannel.md">CreateAuthenticatedChannel(D3D11_1)</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-input.md">D3D11_1DDI_AUTHENTICATED_QUERY_INPUT</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-authenticated-query-output.md">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_QUERYAUTHENTICATEDCHANNEL callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
